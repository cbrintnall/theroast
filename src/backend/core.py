from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from settings import get_settings

import sys

class RoasteryApp:
    def __init__(self):
        self.db = None

        self.app = Flask(__name__)

        settings = get_settings()
        self.app.config.from_object(settings)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self._get_database()
        self.api = Api(self.app)

    def register_resource(self, resource):
        print("HELLO")
        print(resource)

    def _get_database(self):
        template = "postgresql://{username}:{password}@{ip}:{port}/{database}"
        URI = template.format(username=self.app.config.get("POSTGRES_USERNAME"),
                              password=self.app.config.get("POSTGRES_PASSWORD"),
                              ip=self.app.config.get("POSTGRES_HOST"),
                              port=self.app.config.get("POSTGRES_PORT"),
                              database=self.app.config.get("POSTGRES_DATABASE"))
        return URI 

    def init_resources(self):
        pass

    def _init_db(self):
        self.db = SQLAlchemy(self.app) #TODO: Add metadata http://flask-sqlalchemy.pocoo.org/2.3/config/
        self._init_tables()

    def _init_tables(self):
        self.db.create_all()

    def _init_resources(self):
        pass

    def run(self, *args, **kwargs):
        self._init_resources()
        self._init_db()

        self.app.run(*args, **kwargs)