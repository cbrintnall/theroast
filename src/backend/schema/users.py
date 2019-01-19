from marshmallow import Schema, fields, post_load, validates
from marshmallow.exceptions import ValidationError
from models.users import User
from uuid import UUID

class BeanSchema(Schema):
    # Techincal side to user
    _id = fields.UUID(required=True)
    hashed_password = fields.String()

    # About the user
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    bio = fields.String()

    @post_load
    def make_user(self, data):
        return User(**data)

    # class Meta:
    #     unknown = EXCLUDE

