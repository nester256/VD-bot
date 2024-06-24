from conf.config import settings
from src.requests import do_request
from starlette.status import HTTP_201_CREATED


async def send_basket(cart_info: dict) -> bool:
    _, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/orders/create',
        # headers={
        #     'Authorization': f'Bearer {settings.BACKEND_API_KEY}'
        # },
        params={'products': cart_info}
    )
    print({'products': cart_info})
    if status != HTTP_201_CREATED:
        return False
    return True
