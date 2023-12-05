import os
from google.cloud import storage
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET')

storage_client = storage.Client()

bucket = storage_client.get_bucket(bucket_name)

def upload_file(image_file, public):
    if not image_file:
        return None  
    blob = bucket.blob(image_file.filename)
    blob.upload_from_string(image_file.read(), content_type=image_file.content_type)
    if public:
        blob.make_public()
    return blob.public_url

