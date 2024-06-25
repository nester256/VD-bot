from starlette.status import HTTP_201_CREATED

from src.requests import do_request

from conf.config import settings


async def send_basket(cart_info: dict) -> bool:
    _, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/create',
        params={'products': cart_info},
    )
    return status == HTTP_201_CREATED
