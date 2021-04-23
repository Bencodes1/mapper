import sys
import time
import requests
import json


def rastermaker(elevation_grid):  
    ele_raster = []  
    for row in elevation_grid:
        print("here's your current row length:", len(row))
        json_data = json.dumps({"locations": row})
        # print("outgoing json file is:", sys.getsizeof(json_data)/1000000, "megabytes")
        url = 'https://api.open-elevation.com/api/v1/lookup'
        headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json_data)
        json_result = r.json()
        # print('json_result type: ', type(json_result), json_result)

        if r.status_code==200:
            print(f"It worked! Our response json file for this row is", sys.getsizeof(json_result), "bytes")
            results_list = json_result['results']
            list = []
            for result in results_list:
                list.append(result["elevation"])
            
            ele_raster.append(list)
            time.sleep(0.02)
            # for y in range(0,res):
            #     temp_list=[]
            #     for x in range(0,res):
            #         temp_list.append(list[x+row_adder])
            #         # print("fixing our loop, x=", x)
            #         # print("fixing our loop, y=", y)
            #         # print("fixing our loop, row_adder=", row_adder)
            #     row_adder+=res
            #     # print("debug check")
            #     ele_grid.append(temp_list)
        else:
            print("There was an error, status code: ", r.status_code)  
            return(["sorry", "error"])
 
    return(ele_raster)