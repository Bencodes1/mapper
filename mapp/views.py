from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs
from .models import Map
from .gridmaker import latlon_grid_maker
from .rastermaker import rastermaker
from .map_printer import alpha
import sys
import time
import requests
import json
from rest_framework import status
from rest_framework.response import Response



def homepage(response):
    if response.method == 'POST':
        form = MapInputs(response.POST)
        if form.is_valid():
            lat= form.cleaned_data["latitude"]
            lon= form.cleaned_data["longitude"]
            sc = form.cleaned_data["scale"]
            hc = form.cleaned_data["high_color"]
            lc = form.cleaned_data["low_color"]
            xd = form.cleaned_data["x_dim"]
            yd = form.cleaned_data["y_dim"]
            dk = form.cleaned_data["dev_key"]

            # Save map model instance based on user inputs.
            m = Map(latitude=lat, longitude=lon, scale=sc, high_color=hc, low_color=lc, x_dim=xd, y_dim=yd, dev_key=dk)
            m.save()

            # create grid of (latitude, longitude) coordinate pairs around single input location.
            latlon_grid = latlon_grid_maker(m.latitude, m.longitude, m.scale, m.x_dim, m.y_dim )
            
            # iterate through grid, one row at a time, and make request for each one.
            # Generates elevation raster file. 
            elevation_raster = rastermaker(latlon_grid, m.dev_key)

            # Given elevation raster, creates color scaled elevation map. 
            img = alpha(elevation_raster, m.high_color, m.low_color)

            img.save(f"{m.high_color}_to_{m.low_color}.jpg")
            print("Image saved. File size in memory is:", sys.getsizeof(img), "bytes")

            # return HttpResponseRedirect('https://en.wikipedia.org/wiki/Peregrine_falcon')                
            return HttpResponseRedirect('image/')                

        else:
            print("There's a problem with your inputs- here's what we have:")
            print(form.cleaned_data["latitude"])
            print(form.cleaned_data["longitude"])
            print(form.cleaned_data["scale"])
            print(form.cleaned_data["high_color"])
            print(form.cleaned_data["low_color"])
            print(form.cleaned_data["x_dim"])
            print(form.cleaned_data["y_dim"])
            print(form.cleaned_data["dev_key"])


            return HttpResponseRedirect('invalidinputTKTKTK')
    else:
        form = MapInputs()

    return render(response, 'mapp/homepage.html', {'form': form})        


def image_render(request):    
    image = Image.new('RGB', (256,256), (150,120,182))
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response