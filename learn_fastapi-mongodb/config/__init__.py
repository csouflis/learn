from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM_App"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 9000


class DatabaseSettings(BaseSettings):
    # REALM_APP_ID: str = 'example'
    DB_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "test_FARM"


class AuthSettings(BaseSettings):
    JWT_SECRET_KEY: str = 'secret'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SECURE_COOKIE: bool = False


class Settings(CommonSettings, ServerSettings, DatabaseSettings, AuthSettings):
    pass


settings = Settings()
