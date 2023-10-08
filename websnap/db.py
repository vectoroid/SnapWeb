"""
WebSnap -- Database Connection
"""
import logging
from deta import Deta

from .config import get_settings

# init logger
logger = logging.getLogger(__name__)

settings = get_settings()
deta = Deta(settings.deta_app_key)