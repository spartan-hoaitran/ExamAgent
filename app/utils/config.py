
from functools import lru_cache
import os
os.environ["env_path"] = os.path.join(os.path.dirname(__file__), "..", "config/.env")
from typing import Union, List
from pydantic_settings import BaseSettings  # Import BaseSettings from pydantic-settings
from pydantic import Field 

class Settings(BaseSettings):
    # General settings
    API_STR: str = Field(..., env="API_STR")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    PROJECT_DESCRIPTION: str = Field(..., env="PROJECT_DESCRIPTION")
    PROJECT_VERSION: str = Field(..., env="PROJECT_VERSION")
    SERVER_PORT: int = Field(..., env="SERVER_PORT")
    

    # Azure settings
    AZURE_OPENAI_ENDPOINT: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    AZURE_API_VERSION: str = Field(..., env="AZURE_API_VERSION")
    CHAT_COMPLETIONS_MODEL: str = Field(..., env="CHAT_COMPLETIONS_MODEL")
    AZURE_OPENAI_KEY: str = Field(..., env="AZURE_OPENAI_KEY")

    class Config:
        # Read from an .env file if available; otherwise, fallback to os.environ
        env_file = os.environ.get("env_path", ".env")  # Fallback to ".env" if "env_path" not set
        env_file_encoding = "utf-8"
        env_ignore_empty = True
        extra = "ignore"



@lru_cache()
def get_settings() -> Settings:
    
    """Load settings and cache them for reuse."""
    return Settings()
