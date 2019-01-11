from flask import request
from flask.views import MethodView
from schema.beans import BeanSchema
from models.beans import BeansModel
from uuid import uuid4, UUID
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

class Beans(MethodView):
    def generate_id(self):
        return u"{}".format(str(uuid4()))

    def get(self, bean_id=None):
        bean = BeansModel.find_one({"bean_id": UUID(bean_id)})
        schema = BeanSchema()
        response = schema.dumps(bean)
        return response

    def post(self, bean_id=None):
        schema = BeanSchema()
        args = dict(request.values)
        bid = self.generate_id()
        args["bean_id"] = bid

        model = schema.load(args)

        payload = None
        code = 201
        if not model.errors:
            model.data.save()
            payload = {"status":"created"}
            payload["bean_id"] = bid
        else:
            payload = model.errors
            code = 400

        return payload, code

    def put(self, bean_id=None):
        bean = BeansModel.find_one({"bean_id": UUID(bean_id)})
        schema = BeanSchema()

        return {"HOWEDY":"DOO"}

    def delete(self, bean_id=None):
        BeansModel.collection.delete_one({"bean_id": UUID(bean_id)})
        return {"status":"deleted"}