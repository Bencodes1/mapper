import sys
import time
import requests
import json

# Takes elevation files (each one is one 'row' or one horizontal line of 
# pixels in our eventual img), converts list of dicts->json and makes request 
# for that row. Gets response, pulls out elevation values, creating raster file 
# from which map_printer renders. 

def rastermaker(elevation_grid):  
    print("rastermaker started. length of elevation grid:", len(elevation_grid))
    ele_raster = []  
    for row in elevation_grid:
        print("here's your current row length:", len(row))
        json_data = json.dumps({"locations": row})
        url = 'https://api.open-elevation.com/api/v1/lookup'
        headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        start = time.time()

        r = requests.post(url, headers=headers, data=json_data)
        print("troubleshooting, r=", r)
        json_result = r.json()
        if r.status_code==200:
            stop = time.time()
            print(f"It worked! Our response json file for this row is", sys.getsizeof(json_result), "bytes")
            print("time from request to response:", stop - start , "seconds")
            results_list = json_result['results']
            list = []
            for result in results_list:
                list.append(result["elevation"])
            
            ele_raster.append(list)
            time.sleep(0.02)

        else:
            print("There was an error, status code: ", r.status_code)  
            return(["sorry", "error"])
    print("raster file complete, number of rows:", len(ele_raster))
    return(ele_raster)