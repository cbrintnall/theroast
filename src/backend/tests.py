import unittest

from application import application
from utils.endpoint import EndpointView

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()

    def test_app(self):
        self.assertNotEqual(self.app, None)

class TestEndpointsView(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()

    def test_fields_exist(self):
        pass