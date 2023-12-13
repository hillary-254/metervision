"""This module contains the landing page and its multiple pages"""
from django.shortcuts import render


def landingPage(request):
    return render(request, 'landing/index.html')

def featuresPage(request):
    return render(request, 'landing/features.html')

def aboutPage(request):
    return render(request, 'landing/about.html')
