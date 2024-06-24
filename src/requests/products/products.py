from typing import List

from conf.config import settings
from src.requests import do_request
from starlette.status import HTTP_200_OK


async def get_products(offset: int, cat_id: int = None, limit: int = 10) -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/products?limit={limit}&offset={offset}&cat_id={cat_id}',
        method='GET',
        # headers={
        #     'Authorization': f'Bearer {settings.BACKEND_API_KEY}'
        # },
    )
    if status != HTTP_200_OK:
        return None
    return response['products']


async def get_product_info(id: int) -> dict:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/products/product/?id={id}',
        method='GET',
        # headers={
        #     'Authorization': f'Bearer {settings.BACKEND_API_KEY}'
        # },
    )
    if status != HTTP_200_OK:
        return None
    return response
