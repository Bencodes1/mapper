import json
import sys
from decimal import *


def json_gridmaker(lat, lon, scale, high_color, low_color, resolution):
    y_start=lat
    x_start=lon
    lat_lon_list = []
    grid_dict_list = []

    # force resolution to be even (for setting midpoint of grid without issue)
    resolution = 2*int(resolution/2)

    # we want to sync our resolution to our scale. 
    # This is a little tricky because gps 
    # coordinates are in arc seconds, so the 
    # calculation is imprecise: 0.0001 in 
    # decimal coords is ~11meters. 
    # also worth noting: convention is (latidude, longitude). 
    # If we think of gps coords as a grid, this is like (y,x),
    # the opposite of the order we'd expect. 

    meters_per_pixel = (2*scale*1000)/resolution
    iterator= (meters_per_pixel/11) * 0.0001

    for y in range(-int(resolution/2),int(resolution/2)):
        for x in range(-int(resolution/2),int(resolution/2)):
            #generates our json for POST request to open elevation API
            pixel_coords= {
                "latitude": round(y_start + (iterator*y), 5),
                "longitude": round(x_start + (iterator*x), 5)
            }
            lat_lon_list.append(pixel_coords)
            
            #generates list of dicts for us to make our elevation grid later
            # grid_format_coords = {
            #     "x":x, 
            #     "y":y,
            #     "elevation": -(x*y)
            # }
            # grid_dict_list.append(grid_format_coords)

    json_data = json.dumps({"locations": lat_lon_list})
    
    # forgot what this one is doing but it's being annoying 
    # for y in range(0, resolution):
    #     for x in range(0, resolution):
    #         pass
    #         # print("ZZZZZZ", grid_dict_list[x])
    #         #next step is to append xlist here
    #     #and then append xlist to grid here
        

    ###########################################################
    # Debugging json by writing it to files    
    '''
    original_stdout = sys.stdout # Save a reference to the original standard output    
    with open('deleteme.json', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(json_data)
        sys.stdout = original_stdout # Reset the standard output to its original value
    print("lat_lon_list format(entry 3):", lat_lon_list[2])      

    with open('deleteme.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(grid_dict_list)
        sys.stdout = original_stdout # Reset the standard output to its original value
    print("grid_dict_list generated:", grid_dict_list[2]) 
    '''
    ###########################################################

    return(json_data)


    
# def raster_maker(json_response, resolution):
#     return("blank bru")
#     raster = []
#     for y in range(-int(resolution/2),int(resolution/2)):
#         raster_row=[]
#         for x in range(-int(resolution/2),int(resolution/2)):
#             raster_row.append(TK dict positon)
            

# 4th decimal place = 11m.  
# 2 * scale * 1000 = meters in grid
# resolution: each pixel is 1/resolution
# so: 40.96km equals 40,960 m
# each pixel therefore represents 40m
# so, our iterator: 0.0001i = 11m
#40m/11 * 0.0001

# json_gridmaker(41.40917, -122.19579, 20.48, "Red", "Purple", 64)
