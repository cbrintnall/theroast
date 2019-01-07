from flask import request
from flask_api import FlaskAPI
from settings import get_settings

class RoasteryApp(FlaskAPI):
    def __init__(self, *args, **kwargs):
        super(RoasteryApp, self).__init__(*args, **kwargs)
        settings = get_settings()
        self.config.from_object(settings)

    def _get_database(self, app):
        template = "postgresql://{username}:{password}@{ip}:{port}/{database}"
        URI = template.format(username=app.config.get("DATABASE_USERNAME"),
                            password=app.config.get("DATABASE_PASSWORD"),
                            ip=app.config.get("DATABASE_HOST"),
                            port=app.config.get("DATABASE_PORT"))

        return URI
