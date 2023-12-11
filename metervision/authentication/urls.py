# authentication/urls.py

from django.urls import path
from .views import login_view, logout_view, signup_view

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]
