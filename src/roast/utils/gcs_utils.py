from cloudstorage.drivers.google import GoogleStorageDriver
from django.conf import settings

import base64
import uuid

# TODO: Check for support for string uploads
DRIVER = GoogleStorageDriver()
CLIENT = DRIVER.client

def upload_b64(base):
    base64_bytes = base64.b64decode(base)
    container = get_bucket()
    path = generate_path()
    blob = container.blob(path)
    
    blob.upload_from_string(base64_bytes)
    
    return blob.public_url
    
def get_bucket():
    return CLIENT.bucket(settings.GCS_BUCKET)

def generate_path():
    return f"{settings.ENVIRONMENT}/{uuid.uuid4()}"