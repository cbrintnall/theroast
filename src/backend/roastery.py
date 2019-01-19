from flask_api import FlaskAPI
from settings import get_settings
from mongo_thingy import connect
from utils.application import generate_blueprint
from utils.exceptions import RoastError
from flask import jsonify

import os
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

CODE_FIELDS = {"status_code", "code"}

def handle_error(error):
    response = {"error":str(error)}
    status_code = 500

    mutual_fields = set(dir(error)).intersection(CODE_FIELDS)
    if len(mutual_fields) > 0:
        code = getattr(error, list(mutual_fields)[0])
        print(code)
        if type(code) is int:
            status_code = code

    return jsonify(response), status_code

class RoasteryApp(FlaskAPI):
    def __init__(self, *args, **kwargs):
        super(RoasteryApp, self).__init__(*args, **kwargs)

        if not os.environ.get("TESTING"):
            try:
                connect("mongodb://mongo:27017", username="root", password="example")
            except Exception as e:
                LOGGER.warning("Couldn't connect to DB.")

        settings = get_settings()
        self.config.from_object(settings)
        self.register_error_handler(Exception, handle_error)

    def add_endpoint(self, cls):
        url = "/{}".format(cls.__name__.lower())
        bp = generate_blueprint(cls)
        self.register_blueprint(bp, url_prefix=url)
