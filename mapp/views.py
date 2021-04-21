from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from .forms import MapInputs
from .models import Map
from .gridmaker import json_gridmaker
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
            res = form.cleaned_data["resolution"]

            m = Map(latitude=lat, longitude=lon, scale=sc, high_color=hc, low_color=lc, resolution=res)
            m.save()
            json_data = json_gridmaker(m.latitude, m.longitude, m.scale, m.high_color, m.low_color, m.resolution)
            print("outgoing json file is:", sys.getsizeof(json_data)/1000000, "megabytes")

            url = 'https://api.open-elevation.com/api/v1/lookup'
            headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
            r = requests.post(url, headers=headers, data=json_data)
            json_result = r.json()
            print('json_result type: ', type(json_result), json_result)

            if r.status_code==200:
                print("It worked! Our response json file is", sys.getsizeof(json_result), "bytes")
                # results_list = json.dumps(json_result)
                results_list = json_result['results']
                print("results dict is...", type(results_list))
                list = []
                for result in results_list:
                    list.append(result["elevation"])
                
                list_o_lists = []
                row_adder = 0

                for y in range(0,res):
                    temp_list=[]
                    for x in range(0,res):
                        temp_list.append(list[x+row_adder])
                        # print("fixing our loop, x=", x)
                        # print("fixing our loop, y=", y)
                        # print("fixing our loop, row_adder=", row_adder)
                    row_adder+=res
                    # print("debug check")
                    list_o_lists.append(temp_list)

                print("here's your elevations: ")
                print(list_o_lists)


            else:
                print("There was an error, status code: ", r.status_code)    
            
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