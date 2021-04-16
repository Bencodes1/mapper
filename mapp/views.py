import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs
from .models import Map
from .gridmaker import json_gridmaker
import sys

def homepage(request):
    return render(request, "mapp/homepage.html")

def homepage2(response):
    if response.method == 'POST':
        form = MapInputs(response.POST)
        if form.is_valid():
            lat = form.cleaned_data["latitude"]
            lon = form.cleaned_data["longitude"]
            sc = form.cleaned_data["scale"]
            hc = form.cleaned_data["high_color"]
            lc = form.cleaned_data["low_color"]
            res = form.cleaned_data["resolution"]

            m = Map(latitude=lat, longitude=lon, scale=sc, high_color=hc, low_color=lc, resolution=res)
            m.save()
            json_data = json_gridmaker(m.latitude, m.longitude, m.scale, m.high_color, m.low_color, m.resolution)
            print("json file is:", sys.getsizeof(json_data)/1000000, "megabytes")
            return HttpResponseRedirect('image/')
        else:
            return HttpResponseRedirect('invalidinputTKTKTK')
    else:
        form = MapInputs()

    return render(response, 'mapp/homepage2.html', {'form': form})        

# def homepage2(response):
#     form = MapInputs()
#     return render(response, "mapp/homepage2.html", {"form":form})


def image_render(request):    
    image = Image.new('RGB', (256,256), (150,120,182))
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response