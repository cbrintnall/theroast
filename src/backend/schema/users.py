from marshmallow import Schema, fields, post_load, validates, pre_load
from marshmallow.exceptions import ValidationError
from models.users import User
from uuid import UUID, uuid4

import re

class UserSchema(Schema):
    # Technical side to user
    _id = fields.UUID(missing=uuid4)
    password = fields.String(load_only=True, required=True)

    # About the user
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String()
    bio = fields.String()

    @pre_load
    def hash_password(self, data):
        print(data)
        return data

    @validates('username')
    def validate_username(self, value):
        """
            Ensures the username is unique
        """
        pass

    # @validates('password')
    # def validate_password(self, value):
    #     regex = r""

    @post_load
    def make_user(self, data):
        return User(**data)

    # class Meta:
    #     unknown = EXCLUDE

