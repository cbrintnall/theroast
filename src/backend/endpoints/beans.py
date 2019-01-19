from flask import request
from uuid import uuid4, UUID
from schema.beans import BeanSchema
from models.beans import BeansModel
from utils.endpoint import EndpointView

import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

class Beans(EndpointView):
    def __init__(self, *args, **kwargs):
        super(Beans, self).__init__(*args, **kwargs)
        self.schema = BeanSchema
        self.model = BeansModel