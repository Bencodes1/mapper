from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def index(request):
    return HttpResponse("WELCOME to mapper, friend")

def image_render(request):    
    image = Image.new('RGB', (128, 128), 'green')
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response