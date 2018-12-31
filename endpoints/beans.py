from flask import request
from flask_restful import Resource
from sqlalchemy import Table, Column, String, Integer
from marshmallow import Schema, fields
from endpoints import Base, SESSION, ENGINE

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BeanModel(Base):
    __tablename__ = "beans"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    color = Column(String(80), nullable=False)

    def repr(self):
        return "<{} | {}>".format(self.name, self.color)

class BeanSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    color = fields.Str()

class Beans(Resource):
    def get(self, id):
        schema = BeanSchema()
        bean = SESSION.query(BeanModel).get(id)
        return schema.dump(bean)

    def put(self, id):
        return {"method": __name__}

    def delete(self, id):
        return {"method": self.__name__}

    def post(self, id=None):
        schema = BeanSchema(dump_only=["id"])
        validation_errors = schema.validate(request.values)
        print(validation_errors)
        if validation_errors:
            logger.warning("Invalid data provided, returning error.")
            return validation_errors

        loaded_model = schema.load(request.values)
        bean = BeanModel(**loaded_model)
        return schema.dump(bean)
        SESSION.add(bean)
        SESSION.commit()
        return loaded_model