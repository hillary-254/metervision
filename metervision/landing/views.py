from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'landing/index.html')

def featuresPage(request):
    return render(request, 'landing/features.html')

def aboutPage(request):
    return render(request, 'landing/about.html')
