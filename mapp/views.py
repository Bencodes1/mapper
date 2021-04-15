from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs


def homepage(request):
    return render(request, "mapp/homepage.html")

# def homepage2(request):
#     if request.method == 'POST':
#         form = MapInputs(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('mapp/image/')
#     else:
#         form = MapInputs()

#     return render(request, 'homepage2.html', {'form': form})        

def homepage2(response):
    form = MapInputs()
    return render(response, "mapp/homepage2.html", {"form":form})


def image_render(request):    
    image = Image.new('RGB', (256,256), (150,120,182))
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response