from typing import List

from conf.config import settings
from src.requests import do_request
from starlette.status import HTTP_200_OK



async def get_categories(offset: int, limit: int = 5) -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/categories?limit={limit}&offset={offset}',
        method='GET',
        # headers={
        #     'Authorization': f'Bearer {settings.BACKEND_API_KEY}'
        # },
    )
    if status != HTTP_200_OK:
        return None
    return response['categories']