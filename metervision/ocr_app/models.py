from django.db import models
import os
from uuid import uuid4

# Create your models here.

def image_upload_path(instance, filename):
    # Generate a unique filename using UUID4
    unique_filename = str(uuid4())
    _, extension = os.path.splitext(filename)
    return f'uploaded_images/{unique_filename}{extension}'

class Ocr(models.Model):
    uploaded_image = models.ImageField(upload_to=image_upload_path)
    # uploaded_image = models.ImageField(null=True, blank=True, upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)