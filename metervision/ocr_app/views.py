from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import pytesseract

def ocr(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].file
        custom_options = {'config': '--psm 6 outputbase digits'}
        text = perform_ocr(image, custom_options)
        return render(request, 'ocr_app/result.html', {'text': text})
    return render(request, 'ocr_app/index.html')

def perform_ocr(image, custom_options=None):
    img = Image.open(image)
    if custom_options:
        text = pytesseract.image_to_string(img, **custom_options)
    else:
        text = pytesseract.image_to_string(img)
    return text