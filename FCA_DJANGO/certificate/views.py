from django.shortcuts import render

import os
import tempfile
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from pdf2image import convert_from_path
from .models import Certificate
from django.conf import settings


def SearchData(request):
    if 'query' in request.GET:
        query = request.GET['query']
        try:
            data = Certificate.objects.get(certificate_code__icontains = query)
        except:
            data = None
    else:
        data = ''
    context = {
        'data' : data,
    }
    return render(request, 'search.html', context)  


























    # for item in data:
    #     pdf_id = item['certificate_code']
    # pdf = get_object_or_404(Certificate, certificate_code=pdf_id)
    # images = convert_from_path(pdf.certificate.path, poppler_path='D:\Coding\Work\poppler-24.02.0\Library\\bin')
    # for i, image in enumerate(images):
    #     image_path = os.path.join(settings.MEDIA_ROOT, f'certificates/images/{pdf_id}_{i}.png')
    #     if os.path.exists(image_path):
    #         image = image_path
    #     else:
    #         image.save(image_path, 'PNG')
        