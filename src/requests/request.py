from typing import Any, Dict, Optional

import aiohttp
from aiohttp.typedefs import LooseHeaders
from multidict import CIMultiDict
from starlette import status

from src.logger import correlation_id_ctx, logger

from conf.config import settings


class ClientSessionWithCorrId(aiohttp.ClientSession):
    def _prepare_headers(self, headers: Optional[LooseHeaders]) -> CIMultiDict[str]:
        headers = super()._prepare_headers(headers)

        correlation_id = correlation_id_ctx.get()
        headers['X-Correlation-Id'] = correlation_id

        return headers


async def do_request(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    data: Any = None,
    method: str = 'POST',
) -> Any:
    from src.middleware.auth import access_token_cxt

    try:
        headers_ = {'Authorization': f'Bearer {access_token_cxt.get()}'}
    except LookupError:
        headers_ = {}

    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    if headers is not None:
        headers_.update(headers)

    final_exc = None
    async with ClientSessionWithCorrId(
        connector=connector, timeout=timeout, raise_for_status=check_response_status
    ) as session:
        for _ in range(settings.RETRY_COUNT):
            try:
                async with session.request(method, url, headers=headers_, json=params, data=data) as response:
                    if response.content_type == 'application/json' and response.status in (
                        status.HTTP_200_OK,
                        status.HTTP_201_CREATED,
                    ):
                        return await response.json(), response.status
                    return None, response.status
            except aiohttp.ClientResponseError as exc:
                logger.exception('Http error')
                final_exc = exc

    if final_exc is not None:
        raise final_exc

    raise RuntimeError('Unsupported')


async def check_response_status(response: aiohttp.ClientResponse) -> Optional[aiohttp.ClientResponseError]:
    if response.status >= status.HTTP_500_INTERNAL_SERVER_ERROR:
        raise RuntimeError
