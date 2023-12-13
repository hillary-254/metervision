"""This module contains login and signup pages"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signup_view(request):
    """Signup page redirects to dashboard"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:dash')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    """Login page also redirects to dashboard"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dash')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'registration/login.html')

def logout_view(request):
    """Redirects to landing page after logout"""
    logout(request)
    return redirect('landing:landing')
