from flask import request
from flask.views import MethodView
from uuid import uuid4, UUID

class EndpointView(MethodView):
    def __init__(self, *args, **kwargs):
        super(EndpointView, self).__init__(*args, **kwargs)

        self.model = None
        self.schema = None

    def generate_id(self):
        return u"{}".format(str(uuid4()))

    def get(self, uid=None):
        item = self.model.find_one({"_id": UUID(uid)})
        schema = self.schema()
        response = schema.dumps(item)
        return response

    def post(self, uid=None):
        schema = self.schema()
        args = dict(request.values)
        bid = self.generate_id()
        args["_id"] = bid

        model = schema.load(args)

        payload = None
        code = 201
        if not model.errors:
            model.data.save()
            payload = {"status":"created"}
            payload["_id"] = bid
        else:
            payload = model.errors
            code = 400

        return payload, code

    def put(self, uid=None):
        bean = self.model.find_one({"_id": UUID(uid)})
        schema = self.schema()

        return {"test":"test"}

    def delete(self, uid=None):
        self.model.collection.delete_one({"_id": UUID(uid)})
        return {"status":"deleted"}