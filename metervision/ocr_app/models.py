from django.db import models
import os
from uuid import uuid4


def image_upload_path(instance, filename):
    """This module generates a unique id to name uploaded images using UUID4"""
    unique_filename = str(uuid4())
    _, extension = os.path.splitext(filename)
    return f'uploaded_images/{unique_filename}{extension}'

class Ocr(models.Model):
    """OCR class"""
    uploaded_image = models.ImageField(upload_to=image_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
