from marshmallow import Schema, fields, post_load, ValidationError, validates
from flask import request
from flask_restful import Resource
from sqlalchemy import Table, Column, String, Integer, exists
from sqlalchemy.orm import relationship
from endpoints.profile import ProfileSchema, Profile
from helpers import response

import application.application as application
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BeanModel(application.application.db.Model):
    __tablename__ = "beans"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    color = Column(String(80), nullable=False)

    profiles = relationship("Profile")

    def __init__(self, name, color, profile_id=None):
        self.name = name
        self.color = color
        
        if type(profile_id) is int:
            c = SESSION.query(Profile).get(profile_id)
            self.children.append(c)

    def repr(self):
        return "<{} | {}>".format(self.name, self.color)

class BeanSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True,
                      error_messages={'required': 'Please provide a name.'})

    color = fields.Str(required=True,
                       error_messages={'required': 'Please provide a roast color.'})

    profiles = fields.Nested(ProfileSchema)

    @validates('name')
    def validate_name(self, value):
        item = SESSION.query(exists().where(BeanModel.name==value)).scalar()
        if item:
            raise ValidationError("{} already exists, please use another name"
                                  .format(value))

    @post_load
    def make_bean(self, data):
        return BeanModel(**data)

@application.application.register_resource("hi")
class Beans(Resource):
    def get(self, id=None):
        if id is None:
            return response(errors="Please provide an ID.")

        schema = BeanSchema()
        bean = SESSION.query(BeanModel).get(id)
        return schema.dump(bean)

    def put(self, id=None):
        if id is None:
            return response(errors="Please provide an ID.")

        schema = BeanSchema()
        obj = SESSION.query(BeanModel).filter(BeanModel.id == id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        obj.update(request.values)
        SESSION.commit()
        return response(messages={})

    def delete(self, id):
        if id is None:
            return response(errors="Please provide an ID.")

        schema = BeanSchema()
        obj = SESSION.query(BeanModel).get(id)

        if obj is None:
            return response(errors=["Object with id {} does not exist.".format(id)])

        loaded_model = schema.dump(obj)
        SESSION.delete(obj)
        SESSION.commit()
        return response(messages=loaded_model)

    def post(self):
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