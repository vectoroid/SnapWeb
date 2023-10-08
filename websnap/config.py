"""
WebSnap -- Application Configuration
"""
import logging
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

# init logger
log = logging.getLogger(__name__)

class Settings(BaseSettings):
    """
    WebSnap Application Config (settings) class
    """
    app_name: str = "WebSnap d"
    model_config = SettingsConfigDict(env_prefix="WEBSNAP_", env_file=".env", env_file_encoding="utf-8")
    
    # Deta-specific config options (read from enviroment)
    deta_app_key: str 
    

@lru_cache
def get_settings() -> Settings:
    log.info("Loading app config from the environment ...")