from utils.endpoint import EndpointView
from models.users import User
from schema.users import UserSchema

import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

class Users(EndpointView):
    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.schema = UserSchema
        self.model = User