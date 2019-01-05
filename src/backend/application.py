from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from settings import get_settings

class RoasteryApp(Flask):
    def __init__(self, *args, **kwargs):
        super(RoasteryApp, self).__init__(*args, **kwargs)
        settings = get_settings()
        self.config.from_object(settings)
        self.config["SQLALCHEMY_DATABASE_URI"] = _get_database(self)
        self.api = Api(self)
        self.db = SQLAlchemy(self)
        self.db.create_all()

def _get_database(app):
    template = "postgresql://{username}:{password}@{ip}:{port}/{database}"
    URI = template.format(username=app.config.get("POSTGRES_USERNAME"),
                          password=app.config.get("POSTGRES_PASSWORD"),
                          ip=app.config.get("POSTGRES_HOST"),
                          port=app.config.get("POSTGRES_PORT"),
                          database=app.config.get("POSTGRES_DATABASE"))
    return URI 

application = RoasteryApp(__name__)

if __name__ == '__main__':
    application.run(debug=True)
