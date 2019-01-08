from flask import request
from flask.views import MethodView

from models.beans import BeansModel
from random import randint

from models.beans import BeansModel

class Beans(MethodView):    
    def get(self, bean_id=None):
        beans = BeansModel.find_one()
        return {"HEY":"HEY"}

    def post(self, bean_id=None):
        name = str(randint(0, 500))
        b = BeansModel({"name": name})
        b.save()
        return {
            "status": "created",
            "model": "a"
        }

    def put(self, bean_id=None):
        return {"HOWEDY":"DOO"}

    def delete(self, bean_id=None):
        return {"HOWEDY":"DOO"}