import os
from pathlib import Path
from dotenv import load_dotenv

# get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# default to development environment if APP_ENV is not set
APP_ENV = os.getenv("APP_ENV", "development").lower()

# load environment variables from .env files in order of precedence
env_files = [
    BASE_DIR / ".env",
    BASE_DIR / f".env.{APP_ENV}",
    BASE_DIR / f".env.{APP_ENV}.local",
]

for env_file in env_files:
    if env_file.exists():
        print(f"Loading environment file: {env_file}")
        load_dotenv(dotenv_path=env_file, override=True)


# class for centralized settings management
class Settings:
    APP_NAME: str = os.getenv("APP_NAME")
    API_HOST: str = os.getenv("API_HOST")
    API_KEY: str = os.getenv("API_KEY")


# instantiate the singleton object for external import
# 實例化單例物件供外部匯入
settings = Settings()
