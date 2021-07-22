import json
import sys
from decimal import *
import math

def latlon_grid_maker(lat, lon, scale, x_dim, y_dim):
    y_start=lat
    x_start=lon


    # force resolution to be even (for setting midpoint of grid without issue)
    x_dim = 2*int(x_dim/2)
    y_dim = 2*int(y_dim/2)

    # we want to sync our resolution to our scale. 
    # This is a little tricky because gps 
    # coordinates are in arc seconds, so the 
    # calculation is imprecise: 0.0001 in 
    # decimal coords is ~11meters. 
    # to be more specific: one degree of latitude @ equator is 110.567 km, @ pole is 111.699 km. we just take a rough estimate between these. 

    # also worth noting: convention is (latidude, longitude). 
    # If we think of gps coords as a grid, this is like (y,x),
    # the opposite of the order we'd expect. 

    meters_per_pixel = (2*scale*1000)/y_dim
    iterator= (meters_per_pixel/111321) 
    # print("gridmaker2 latitude iterator", iterator)
    
    latlon_grid = []
    for y in range(-int(y_dim/2),int(y_dim/2)):
        loop_lat = round(y_start + (iterator*y), 7)

        # take latitude iterator, and multiply it 
        # by a ratio based on the latitude. 
        # (longitude decimal -> km declines with
        # distance from the equator. we use trig
        # function to make approx. adjustment)

        lon_ratio = math.cos(((2*math.pi)/360)*loop_lat)
        lon_iterator = lon_ratio*iterator 
        # print("gridmaker2 longitude iterator",lon_iterator)

        latlon_row = []
        for x in range(-int(x_dim/2),int(x_dim/2)):
            loop_lon = round(x_start + (lon_iterator*x), 7)
            latlon_row.append(loop_lat)
            latlon_row.append(loop_lon)
        
        latlon_grid.append(latlon_row)    
    print("gridmaker finished running, length of last row:", len(latlon_row))
    return(latlon_grid)    

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