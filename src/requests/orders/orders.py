from typing import List

from starlette.status import HTTP_200_OK

from src.requests import do_request

from conf.config import settings


async def get_orders() -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/list',
        method='GET',
    )
    if status != HTTP_200_OK:
        return None
    return response['orders']


async def get_awaiting_orders() -> List:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/list_to_delivery',
        method='GET',
    )
    if status != HTTP_200_OK:
        return None
    return response['orders']


async def create_delivery(order_id: int) -> bool:
    _, status = await do_request(f'{settings.BACKEND_HOST}/api/v1/orders/create_delivery/{order_id}', method='GET')
    return status == HTTP_200_OK


async def get_active() -> list:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/list_active',
        method='GET',
    )
    if status != HTTP_200_OK:
        return None
    return response['orders']


async def set_done(order_id: int) -> bool:
    _, status = await do_request(f'{settings.BACKEND_HOST}/api/v1/orders/delivery_done/{order_id}', method='GET')
    return status == HTTP_200_OK
