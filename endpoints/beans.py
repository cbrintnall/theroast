from marshmallow import Schema, fields, post_load, ValidationError, validates
from flask import request
from flask_restful import Resource
from sqlalchemy import Table, Column, String, Integer, exists
from endpoints import Base, SESSION, ENGINE
from helpers import response

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
    name = fields.Str(required=True,
                      error_messages={'required': 'Please provide a name.'})

    color = fields.Str(required=True,
                       error_messages={'required': 'Please provide a roast color.'})

    @validates('name')
    def validate_name(self, value):
        item = SESSION.query(exists().where(BeanModel.name==value)).scalar()
        if item:
            raise ValidationError("{} already exists, please use another name"
                                  .format(value))

    @post_load
    def make_bean(self, data):
        return BeanModel(**data)

class Beans(Resource):
    def get(self, id):
        schema = BeanSchema()
        bean = SESSION.query(BeanModel).get(id)
        return schema.dump(bean)

    def put(self, id):
        schema = BeanSchema()
        obj = SESSION.query(BeanModel).filter(BeanModel.id == id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        obj.update(request.values)
        SESSION.commit()
        return response(messages={})

    def delete(self, id):
        schema = BeanSchema()
        obj = SESSION.query(BeanModel).get(id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        loaded_model = schema.dump(obj)
        SESSION.delete(obj)
        SESSION.commit()
        return response(messages=loaded_model)

    def post(self, id=None):
        schema = BeanSchema(dump_only=["id"])
        data = request.form
        loaded_model = schema.load(data)
        
        if loaded_model.errors:
            return loaded_model.errors

        model = loaded_model.data
        SESSION.add(model)
        SESSION.commit()

        viewable_data = schema.dump(model)
        return response(messages=viewable_data)