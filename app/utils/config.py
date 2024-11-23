
from functools import lru_cache
import os
from typing import Optional, Union
from pydantic_settings import BaseSettings, SettingsConfigDict
os.environ["env_path"] = os.path.join(os.path.dirname(__file__), "..", "config/.env")
class Settings(BaseSettings):
    # General settings
    API_STR: str
    SECRET_KEY: str
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    PROJECT_VERSION: str
    SERVER_PORT:int
    BACKEND_CORS_ORIGINS: Union[str, None] = ["*"]
    
    # Database settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    # Azure settings
    AZURE_OPENAI_ENDPOINT: str
    AZURE_API_VERSION: str
    CHAT_COMPLETIONS_MODEL: str
    AZURE_OPENAI_KEY:str

    model_config = SettingsConfigDict(env_file=os.environ["env_path"], env_file_encoding="utf-8")


@lru_cache()
def get_settings() -> Settings:
    
    """Load settings and cache them for reuse."""
    return Settings()
