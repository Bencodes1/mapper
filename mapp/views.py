from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

def homepage(request):
    # return HttpResponse("WELCOME to mapper, friend")
    return render(request, "mapp/homepage.html")

def image_render(request):    
    image = Image.new('RGB', (256,256), (150,120,182))
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response