from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    WEBHOOK_URL: str = ''

    REDIS_HOST: str = 'redis'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str
    REDIS_DB: int = 0

    LOG_LEVEL: str = ''

    RETRY_COUNT: int = 3

    DEFAULT_ERROR_MSG: str = 'Произошла ошибка, попробуйте ещё раз'

    BACKEND_HOST: str = 'http://web:8000'

    MENU_PHOTO: str = 'https://png.klev.club/uploads/posts/2024-04/png-klev-club-ccvi-p-nadpis-menyu-png-13.png'

    CATEGORIES_PHOTO: str = 'https://ogneborec.su/files/uploads/images/Raschet_kategoriy_pomesheniy__montazh_OPS.jpg'

    DEFAULT_PRODUCT_PHOTO: str = 'https://www.tiffincurry.ca/wp-content/uploads/2021/02/default-product.png'

    NEW_CUSTOMER_ADDR: str = 'Пока не задан'

    NOTHING_ERROR_MSG: str = 'По указанной странице ничего не найдено'


settings = Settings()
