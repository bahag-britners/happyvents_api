import io
import os
from PIL import Image
from google.cloud import storage
bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET')

storage_client = storage.Client()

bucket = storage_client.get_bucket(bucket_name)

def upload_file(image_file, public):
    if not image_file:
        return None  
    image = Image.open(image_file)
    optimized_image_file = io.BytesIO()
    image.save(optimized_image_file, format=image.format, optimize=True)
    optimized_image_file.seek(0)

    blob = bucket.blob(image_file.filename)
    blob.upload_from_string(optimized_image_file.read(), content_type=image_file.content_type)

    return blob.public_url

