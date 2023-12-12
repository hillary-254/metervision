# dashboard/urls.py
from django.urls import path
from .views import dash

app_name = 'dashboard'

urlpatterns = [
    path('', dash, name='dash'),
]
