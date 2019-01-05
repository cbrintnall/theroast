import os
import sys
import logging

class Settings:
    logger = logging.getLogger(__name__)
    POSTGRES_USERNAME   = os.environ.get("POSTGRES_USERNAME")
    POSTGRES_PASSWORD   = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DATABASE   = os.environ.get("POSTGRES_DATABASE")
    POSTGRES_HOST       = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT = 5432

class NonprodSettings(Settings):
    pass

class ProdSettings(Settings):
    pass

def get_settings():
    key = os.environ.get("APP_SETTINGS"," nonprod")
    if key is "nonprod":
        return NonprodSettings()
    if key is "prod":
        return ProdSettings()
    return NonprodSettings()
