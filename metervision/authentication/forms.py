# In forms.py inside your app

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')