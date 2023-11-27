from django.shortcuts import render
import easyocr


def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        reader = easyocr.Reader(['en'])  # Specify language
        results = reader.readtext(image)
        return render(request, 'easy_ocr/result.html', {'image': image, 'results': results})
    return render(request, 'easy_ocr/upload.html')