from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from endpoints.beans import Beans, BeanModel
from endpoints import ENGINE
from settings import get_settings

class RoasteryApp:
    def __init__(self):
        self.app = Flask(__name__)

        settings = get_settings()
        self.app.config.from_object(settings)
        self.api = Api(self.app)

    def init_resources(self):
        self.api.add_resource(Beans, "/beans/<string:id>")
        
    def init_tables(self):
        if not ENGINE.dialect.has_table(ENGINE, "beans"):
            BeanModel.__table__.create(ENGINE)

    def run(self, *args, **kwargs):
        self.init_resources()
        self.init_tables()

        self.app.run(*args, **kwargs)

def get_app(*args, **kwargs):
    return RoasteryApp()

application = get_app()

if __name__ == '__main__':
    application.run(debug=True)
