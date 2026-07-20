import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "V2MarzNet"
    )

    DATABASE_HOST = os.getenv(
        "DATABASE_HOST"
    )

    REDIS_HOST = os.getenv(
        "REDIS_HOST"
    )


settings = Settings()
