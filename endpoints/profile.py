from marshmallow import Schema, fields, post_load, ValidationError, validates
from flask import request
from flask_restful import Resource
from sqlalchemy import Table, Column, String, Integer, exists
from endpoints import Base, SESSION, ENGINE
from helpers import response

import logging
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)

    def repr(self):
        return "{}".format(self.name)

class ProfileSchema(Schema):
    name = fields.Str(required=True)

    @validates('name')
    def validate_name(self, value):
        item = SESSION.query(exists().where(Profile.name==value)).scalar()
        if item:
            raise ValidationError("{} already exists, please use another name"
                                  .format(value))

        if not re.match("[^\d]+", value):
            raise ValidationError("Please enter only charaters.")

    @post_load
    def load_object(self, data):
        return Profile(**data)

class ProfileEndpoint(Resource):
    def get(self, id):
        schema = ProfileSchema()
        bean = SESSION.query(Profile).get(id)
        return schema.dump(bean)

    def put(self, id):
        schema = ProfileSchema()
        obj = SESSION.query(Profile).filter(Profile.id == id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        obj.update(request.values)
        SESSION.commit()
        return response(messages={})

    def delete(self, id):
        schema = ProfileSchema()
        obj = SESSION.query(Profile).get(id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        loaded_model = schema.dump(obj)
        SESSION.delete(obj)
        SESSION.commit()
        return response(messages=loaded_model)

    def post(self):
        schema = ProfileSchema(dump_only=["id"])
        data = request.form
        loaded_model = schema.load(data)
        
        if loaded_model.errors:
            return loaded_model.errors

        model = loaded_model.data
        SESSION.add(model)
        SESSION.commit()

        viewable_data = schema.dump(model)
        return response(messages=viewable_data)