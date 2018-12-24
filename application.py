from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from endpoints.beans import Beans
from settings import get_settings

class RoasteryApp:
    def __init__(self):
        self.app = Flask(__name__)

        settings = get_settings()
        self.app.config.from_object(settings)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////C:\\tmp\\test.db'

        self.api = Api(self.app)
        self.db = SQLAlchemy(self.app)
        self.connection = self.db.make_connector()
        
        self.api.add_resource(Beans, "/beans/<string:id>")

    def run(self, *args, **kwargs):
        self.db.create_all()
        self.app.run(*args, **kwargs)

def get_app(*args, **kwargs):
    return RoasteryApp()

application = get_app()

if __name__ == '__main__':
    application.run(debug=True)
