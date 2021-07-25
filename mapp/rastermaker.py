import sys
import time
import requests
import json
# xxxxx

# Takes elevation files (each one is one 'row' or one horizontal line of 
# pixels in our eventual img), converts list of dicts->json and makes request 
# for that row. Gets response, pulls out elevation values, creating raster file 
# from which map_printer renders. 

def rastermaker(latlon_grid, dev_key):  
    print("rastermaker started. length of elevation grid:", len(latlon_grid))
    ele_raster = []  
    for row in latlon_grid:
        print("here's your current row length: ", len(row))
        # print("here's your current row: ", row)
        json_data = json.dumps({"latLngCollection": row})
        url = 'http://open.mapquestapi.com/elevation/v1/profile?key='+dev_key
        headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        start = time.time()

        r = requests.post(url, headers=headers, data=json_data)
        json_result = r.json()
        if r.status_code==200:
            stop = time.time()
            # print(f"It worked! Our response json file for this row is", sys.getsizeof(json_result), "bytes")
            print("time from request to response:", stop - start , "seconds")
            results_list = json_result['elevationProfile']
            list = []
            for result in results_list:
                list.append(result["height"])
            
            ele_raster.append(list)
            time.sleep(0.02)

        else:
            print("troubleshooting, r=", r)
            print("There was an error, status code: ", r.status_code)  
            return(["sorry", "error"])
    print("raster file complete, number of rows:", len(ele_raster))
    '''
    original_stdout = sys.stdout # Save a reference to the original standard output    
    with open('durham_auto.json', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(ele_raster)
        sys.stdout = original_stdout # Reset the standard output to its original value
    print('durham auto saved')

    '''
    return(ele_raster)


