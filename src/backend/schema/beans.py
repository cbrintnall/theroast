from marshmallow import Schema, fields

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

