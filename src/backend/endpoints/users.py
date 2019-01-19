from flask import request
from uuid import uuid4, UUID
from utils.endpoint import EndpointView
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)