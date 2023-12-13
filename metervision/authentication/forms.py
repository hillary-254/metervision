from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your email'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirm your password'}),
        } # these don't seem to work
