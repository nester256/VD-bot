from typing import List

from starlette.status import HTTP_200_OK

from src.requests import do_request

from conf.config import settings


async def get_categories(offset: int, limit: int = 5) -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/categories?limit={limit}&offset={offset}',
        method='GET',
    )
    if status != HTTP_200_OK:
        return None
    return response['categories']
