from django.urls import path
from .views import *

app_name = 'landing'

urlpatterns = [
    path('', landingPage, name='landing'),
    path('features/', featuresPage, name='features'),
    path('about/', aboutPage, name='about'),
]