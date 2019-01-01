from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from endpoint.core import Endpoint
from endpoints.beans import Beans, BeanModel
from endpoints.profile import Profile, ProfileEndpoint
from endpoints import ENGINE
from settings import get_settings

class RoasteryApp:
    def __init__(self):
        self.app = Flask(__name__)

        settings = get_settings()
        self.app.config.from_object(settings)
        self.api = Api(self.app)

    def init_resources(self):
        self.api.add_resource(Beans, "/beans", "/beans/<string:id>")
        self.api.add_resource(ProfileEndpoint, "/profiles", "/profiles/<string:id>")
    
    def _check_for_table(self, table):
        return ENGINE.dialect.has_table(ENGINE, table)

    def init_tables(self):
        # TODO: Move table names to own file.
        # Link Model class name and table together.
        # Might need to make another object for that.
        if not self._check_for_table("beans"):
            BeanModel.__table__.create(ENGINE)

        if not self._check_for_table("profiles"):
            Profile.__table__.create(ENGINE)

    def run(self, *args, **kwargs):
        self.init_resources()
        self.init_tables()

        self.app.run(*args, **kwargs)

def get_app(*args, **kwargs):
    return RoasteryApp()

application = get_app()

if __name__ == '__main__':
    application.run(debug=True)
