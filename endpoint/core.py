from marshmallow import Schema, fields, post_load, ValidationError, validates
from flask import request
from flask_restful import Resource
from sqlalchemy import Table, Column, String, Integer, exists
from endpoints import Base, SESSION, ENGINE
from helpers import response

import logging

class Endpoint(Resource):
    def __init__(self):
        super(Endpoint, self).__init__()

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