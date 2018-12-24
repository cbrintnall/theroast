from flask_restful import Resource

class Beans(Resource):
    def get(self, id):
        return {"method": "GET"}

    def put(self, id):
        return {"method": __name__}

    def delete(self, id):
        return {"method": self.__name__}

    def post(self, id=None):
        return {"method": "P{OST"}