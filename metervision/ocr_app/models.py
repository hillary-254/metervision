from django.db import models

# Create your models here.

class Ocr(models.Model):
    image_url = models.ImageField(null=True, blank=True, upload_to="images/")