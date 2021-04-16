from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs
from .models import Map


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
        return HttpResponseRedirect('image/')
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