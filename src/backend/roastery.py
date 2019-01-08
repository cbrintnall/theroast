from flask import request
from flask_api import FlaskAPI
from settings import get_settings
from pymongo import MongoClient

class RoasteryApp(FlaskAPI):
    def __init__(self, *args, **kwargs):
        super(RoasteryApp, self).__init__(*args, **kwargs)
        self.db = MongoClient('mongo', 27017)
        settings = get_settings()
        self.config.from_object(settings)
