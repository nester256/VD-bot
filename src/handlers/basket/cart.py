import json
from typing import List

from aiogram import types

from src.buttons.basket.getter import get_basket_buttons
from src.integrations.redis import redis


async def get_cart_summary(user_id: int) -> dict:
    cart = await get_cart(user_id)
    summary = {}
    for item in cart:
        item_id = str(item['id'])
        if item_id in summary:
            summary[item_id] += 1
        else:
            summary[item_id] = 1
    return summary


async def get_cart(user_id: int) -> List:
    cart_data = await redis.get(f'cart-{user_id}')
    if cart_data:
        return json.loads(cart_data)
    return []


async def add_to_cart(user_id: int, product: dict) -> None:
    cart = await get_cart(user_id)
    cart.append(product)
    await redis.set(f'cart-{user_id}', json.dumps(cart))


async def remove_from_cart(user_id: int, product_id: int) -> None:
    cart = await get_cart(user_id)
    cart = [product for product in cart if product['id'] != product_id]
    await redis.set(f'cart-{user_id}', json.dumps(cart))


async def send_cart_buttons(cart: list, callback: types.CallbackQuery) -> None:
    if cart:
        total_price = sum(item['price'] for item in cart)
        await callback.message.answer(text=f'Ваша корзина: ₽{total_price}', reply_markup=get_basket_buttons(cart))
    else:
        await callback.message.answer('Ваша корзина пуста.')


async def clear_cart(user_id: int):
    await redis.delete(f'cart-{user_id}')
