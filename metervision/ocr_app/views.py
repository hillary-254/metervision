from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import pytesseract
import easyocr

def ocr(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].file
        selected_ocr = request.POST.get('ocr_type', 'pytesseract')  # Default to pytesseract if not specified
        custom_options = {'config': '--psm 6 outputbase digits'}

        if selected_ocr == 'pytesseract':
            text = pytesseract_ocr(image, custom_options)
            return render(request, 'ocr_app/result.html', {'text': text})
        elif selected_ocr == 'easyocr':
            results = easyocr_ocr(image)
            return render(request, 'easy_ocr/result.html', {'image': image, 'results': results})
        elif selected_ocr == 'both':
            text = pytesseract_ocr(image, custom_options)
            results = easyocr_ocr(image)
            return render(request, 'ocr_app/result.html', {'text': text, 'image': image, 'results': results})

    return render(request, 'ocr_app/index.html')


def pytesseract_ocr(image, custom_options=None):
    img = Image.open(image)
    if custom_options:
        text = pytesseract.image_to_string(img, **custom_options)
    else:
        text = pytesseract.image_to_string(img)
    return text


def easyocr_ocr(image):
    image_data = Image.open(image)
    reader = easyocr.Reader(['en'])  # Specify language
    results = reader.readtext(image_data)
    return results