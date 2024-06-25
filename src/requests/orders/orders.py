from typing import List

from starlette.status import HTTP_200_OK

from src.requests import do_request

from conf.config import settings


async def get_orders() -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/list',
        method='GET',
        # headers={
        #     'Authorization': f'Bearer {settings.BACKEND_API_KEY}'
        # },
    )
    if status != HTTP_200_OK:
        return None
    return response['orders']
