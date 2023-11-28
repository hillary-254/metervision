"""This module contains the OCR engines"""
from django.shortcuts import render
from PIL import Image
import pytesseract
import easyocr
import numpy as np


def ocr(request):
    """This module calls pytesseract and easyocr"""
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].file
        selected_ocr = request.POST.get('ocr_type', 'pytesseract')  # Default to pytesseract if not specified
        custom_options = {'config': '--psm 6 outputbase digits'}

        if selected_ocr == 'pytesseract':
            text = pytesseract_ocr(image, custom_options)
            return render(request, 'ocr_app/result.html', {'text': text})
        elif selected_ocr == 'easyocr':
            results = easy_ocr(image)
            return render(request, 'ocr_app/result.html', {'image': image, 'results': results})
        elif selected_ocr == 'both':
            text = pytesseract_ocr(image, custom_options)
            results = easy_ocr(image)
            return render(request, 'ocr_app/result.html', {'text': text, 'image': image, 'results': results})
    return render(request, 'ocr_app/index.html')


def pytesseract_ocr(image, custom_options=None):
    """Runs pytesseract engine"""
    img = Image.open(image)
    if custom_options:
        text = pytesseract.image_to_string(img, **custom_options)
    else:
        text = pytesseract.image_to_string(img)
    return text


def easy_ocr(image):
    """Runs easyocr engine"""
    image_data = Image.open(image)
    reader = easyocr.Reader(['en'], gpu=False)  # Specify language and cpu mode
    results = ' '.join([item[1] for item in reader.readtext(np.array(image_data))])  # Convert image to numpy array
    return results
