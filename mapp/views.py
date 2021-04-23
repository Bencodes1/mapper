from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs
from .models import Map
from .gridmaker import ele_grid_maker
from .rastermaker import rastermaker
from .map_printer import alpha
import sys
import time
import requests
import json
from rest_framework import status
from rest_framework.response import Response


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
            xd = form.cleaned_data["x_dim"]
            yd = form.cleaned_data["y_dim"]

            m = Map(latitude=lat, longitude=lon, scale=sc, high_color=hc, low_color=lc, x_dim=xd, y_dim=yd)
            m.save()
            elevation_grid = ele_grid_maker(m.latitude, m.longitude, m.scale, m.x_dim, m.y_dim )
            
            elevation_raster = rastermaker(elevation_grid) # iterate through grid, one row at a time, and make request for each one.

            img = alpha(elevation_raster, m.high_color, m.low_color)
            print("hope this worked... img size is:", sys.getsizeof(img))

            img.save(f"{m.high_color} to {m.low_color}")
            # save elevation raster to file          
            # original_stdout = sys.stdout # Save a reference to the original standard output    
            # with open('shasta.txt', 'w') as f:
            #     sys.stdout = f # Change the standard output to the file we created.
            #     print(elevation_raster)
            #     sys.stdout = original_stdout # Reset the standard output to its original value

            return HttpResponseRedirect('image/')                

        else:
            return HttpResponseRedirect('invalidinputTKTKTK')
    else:
        form = MapInputs()

    return render(response, 'mapp/homepage2.html', {'form': form})        


# def external_api_view(request):
#     if request.method == "POST":
#         attempt_num = 0  # keep track of how many times we've retried
#         while attempt_num < 5:
#             url = 'https://api.open-elevation.com/api/v1/lookup'
#             headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
#             r = requests.get(url, headers=headers)

#             payload = {'Token':'My_Secret_Token','product':request.POST.get("options"),'price':request.POST.get("price")}
#             response = requests.post(url, headers=headers, data = payload)
#             if r.status_code == 200:
#                 data = r.json()
#                 return Response(data, status=status.HTTP_200_OK)
#             else:
#                 attempt_num += 1
#                 # You can probably use a logger to log the error here
#                 time.sleep(5)  # Wait for 5 seconds before re-trying
#         return Response({"error": "Request failed"}, status=r.status_code)
#     else:
#         return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)



def image_render(request):    
    image = Image.new('RGB', (256,256), (150,120,182))
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, "JPEG")
    return response