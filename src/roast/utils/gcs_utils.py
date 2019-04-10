from cloudstorage.drivers.google import GoogleStorageDriver
from django.conf import settings

import logging
import base64
import uuid

# TODO: Check for support for string uploads
DRIVER = GoogleStorageDriver()
CLIENT = DRIVER.client

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def upload_b64(base):
    base64_bytes = base64.b64decode(base)
    container = get_bucket()
    path = generate_new_path()
    blob = container.blob(path)
    
    blob.upload_from_string(base64_bytes)
    
    return blob.public_url

def get_image(unique_id):
    bucket = get_bucket()
    true_id = unique_id
    if '-' not in unique_id:
        true_id = ndtd(unique_id)
    image = None
    try:
        print(f"Grabbing image {true_id}")
        image = bucket.get_blob(generate_path(true_id))
    except:
        print("")

    return image

def ndtd(unique_id):
    """
    No dash to dash, a method to convert a
    UUID without dashes, into one with them,
    according to UUID spec.
    """
    final_value = unique_id
    for val in (8, 13, 18, 23):
        final_value = f"{final_value[:val]}-{final_value[val:]}"
    return final_value

def dtnd(unique_id):
    """
    Dash to no dash, the opposite of ndtd,
    used to remove dashes from a UUID4
    """
    return unique_id.replace('-', '')

def get_bucket():
    return CLIENT.bucket(settings.GCS_BUCKET)

def generate_path(unique_id):
    return f"{settings.ENVIRONMENT}/{unique_id}"

def get_id_from_path(path):
    full_path = path.split('/')
    return full_path[len(full_path)-1]

def generate_new_path():
    return generate_path(uuid.uuid4())