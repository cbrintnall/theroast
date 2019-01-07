from flask import request
from flask.views import MethodView

from models.beans import BeansModel
from random import randint

class Beans(MethodView):
    def get(self, version=None):
        beans = BeansModel.find_one(version=version)
        return {"model":beans}

    def post(self, version=None):
        print("HELLO?")
        beans = BeansModel(name=randint(0, 500))
        beans.save()
        return {
            "status": "created",
            "model": beans
        }

    def put(self, version=None):
        return {"HOWEDY":"DOO"}

    def delete(self, version=None):
        return {"HOWEDY":"DOO"}