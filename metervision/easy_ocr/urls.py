from django.urls import path
from .views import easy_ocr

urlpatterns = [
    path('', easy_ocr, name='easy_ocr'),
]
