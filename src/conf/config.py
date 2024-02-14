from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TINDER_BACKEND_HOST: str = "http://localhost:8000"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 1
    BOT_TOKEN: str = "6711482436:AAEGDu3egWfcvjlYV2CFwHfKNe-tIRshjSs"
    # REDIS_PASSWORD: str
    # REDIS_SIRIUS_CACHE_PREFIX: str = 'sirius'


settings = Settings()
