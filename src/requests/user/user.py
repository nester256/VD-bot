from typing import Optional

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.requests import do_request

from conf.config import settings


async def create_user_request(id: int, username: str) -> bool:
    _, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/auth/register',
        params={'id': id, 'username': username},
    )
    return status == HTTP_201_CREATED


async def get_user_token_request(user_id: int) -> Optional[str]:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/auth/login',
        params={'id': user_id},
    )
    if status != HTTP_200_OK:
        return None

    return response['access_token']


async def get_user_info() -> dict:
    response, status = await do_request(
        f'{settings.BACKEND_HOST}/api/v1/auth/info',
        method='GET',
    )
    if status != HTTP_200_OK:
        return None
    info = {'id': response['id'], 'role': response['role'], 'address': response['address']}
    return info
