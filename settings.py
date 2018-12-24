import os
import sys
import logging

class Settings:
    logger = logging.getLogger(__name__)

class NonprodSettings(Settings):
    pass

class ProdSettings(Settings):
    pass

def get_settings():
    key = os.environ.get("APP_SETTINGS")
    if key == "nonprod":
        NonprodSettings()
    if key == "prod":
        return ProdSettings()
    return NonprodSettings()