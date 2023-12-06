"""This module opens an image, reads, saves it then runs the OCR engines"""
from django.shortcuts import render
from PIL import Image
import pytesseract
import easyocr
import numpy as np
import os
from django.conf import settings
from .models import Ocr
import uuid


def ocr(request):
    """This module calls pytesseract and easyocr"""
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].file
        selected_ocr = request.POST.get('ocr_type', 'pytesseract')
        custom_options = {'config': '--psm 6 outputbase digits'} # pytesseract input options

        # Save the uploaded image and its path to the database
        image_url = save_uploaded_image(image)

        if selected_ocr == 'pytesseract':
            text = pytesseract_ocr(image, custom_options)
            return render(request, 'ocr_app/index.html', {'text': text, 'image_url': image_url})
        elif selected_ocr == 'easyocr':
            results = easy_ocr(image)
            return render(request, 'ocr_app/index.html', {'image_url': image_url, 'results': results})
        elif selected_ocr == 'both':
            text = pytesseract_ocr(image, custom_options)
            results = easy_ocr(image)
            return render(request, 'ocr_app/index.html', {'text': text, 'image_url': image_url, 'results': results})
    return render(request, 'ocr_app/index.html', {'image_url': None})



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

def save_uploaded_image(image):
    """This module saves uploaded image to file and database"""
    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.jpg"

    # Save the uploaded image to a temporary location
    image_data = Image.open(image)
    
    # Convert the image to RGB mode if it has an alpha channel
    if image_data.mode == 'RGBA':
        image_data = image_data.convert('RGB')

    # Construct the full path to save the image
    image_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

    # Save the image
    image_data.save(image_path)

    # Save the relative path to the database
    relative_path = os.path.relpath(image_path, settings.MEDIA_ROOT)
    Ocr.objects.create(uploaded_image=relative_path)

    # Return the full path for potential further use
    return image_path