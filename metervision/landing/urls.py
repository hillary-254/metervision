from django.urls import path
from .views import landingPage

app_name = 'landing'

urlpatterns = [
    path('', landingPage, name='landing'),
]