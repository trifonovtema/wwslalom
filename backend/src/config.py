from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION")
    ALEMBIC_VERSION_SCHEMA = os.getenv("ALEMBIC_VERSION_SCHEMA")

    RESET_PASSWORD_TOKEN_SECRET = os.getenv("RESET_PASSWORD_TOKEN_SECRET")
    VERIFICATION_TOKEN_SECRET = os.getenv("VERIFICATION_TOKEN_SECRET")
    GENERATE_TOKEN_SECRET = os.getenv("GENERATE_TOKEN_SECRET")
