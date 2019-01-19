from flask_api import FlaskAPI
from settings import get_settings
from mongo_thingy import connect
from utils.application import generate_blueprint

import os
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

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

    def add_endpoint(self, cls):
        url = "/{}".format(cls.__name__.lower())
        bp = generate_blueprint(cls)
        self.register_blueprint(bp, url_prefix=url)
