from marshmallow import Schema, fields, post_load, validates
from marshmallow.exceptions import ValidationError
from models.beans import BeansModel

class BeanSchema(Schema):
    bean_id = fields.UUID()
    name = fields.Str(required=True,
                      error_messages={'required': 'Please provide a name.'})

    color = fields.Str(required=True,
                       error_messages={'required': 'Please provide a roast color.'})

    # profiles = fields.Nested(ProfileSchema)

    @validates('name')
    def validate_name(self, value):
        item = BeansModel.find_one({"name": value})
        if item:
            raise ValidationError("{} already exists, please use another name"
                                  .format(value))

    @post_load
    def make_bean(self, data):
        return BeansModel(**data)

    # class Meta:
    #     unknown = EXCLUDE

