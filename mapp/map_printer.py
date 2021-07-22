import random 
import time
import sys
from PIL import Image, ImageColor
from colour import Color


def alpha(raster, high_color, low_color):
    xy_grid=raster
    color_img   = map_create(xy_grid, high_color, low_color)
    return(color_img)

# Takes xy_grid, creates color-scaled topo map. 
def map_create(xy_grid, high_color, low_color):
    min_ele, max_ele = min_and_max(xy_grid)  
    increment   = gradient_scaler(min_ele, max_ele)
    start = time.time()

    RGB_list    = gradient_creator(low_color, high_color)
    img         = Image.new('RGB', (len(xy_grid[0]), len(xy_grid)))
    for rownum in range(0, len(xy_grid)-1):
        for pos in range(0, len(xy_grid[0])-1):
            curr_ele = xy_grid[rownum][pos]
            curr_colornum = abs(int(ele_to_col_val(curr_ele, min_ele, increment)))-1
            # print(curr_colornum)
            curr_RGB = RGB_list[curr_colornum]
            img.putpixel((pos, rownum), curr_RGB)            
    stop = time.time()
    color_timer = stop - start
    
    print("Image complete. Time to draw: ", color_timer, "seconds")   
    print("map_printer img file size is:", sys.getsizeof(img), "bytes")           
    return(img)     

# Returns overall max and min values in whole map. 
# Used to scale color scheme. 
def min_and_max(xy_grid):
    temp_minlist = []
    temp_maxlist = []
    for row in range(0, len(xy_grid)-1):
        temp_minlist.append(min(xy_grid[row]))
        temp_maxlist.append(max(xy_grid[row]))
    min_ele = min(temp_minlist)     
    max_ele = max(temp_maxlist)     
    return(min_ele, max_ele)


# Takes range of elevations, scales to 256 increments for coloring.
def gradient_scaler(min_ele, max_ele):
    range = max_ele - min_ele
    print ('Gradient Scaled. Range:', range)
    return(range/256)


# Given highest and lowest color, creates spectrum btwn 2
# with 256 colors (in list form).
def gradient_creator(high_color, low_color):
    start_col = Color(low_color) 
    stop_col  = Color(high_color) 
    hex_colors = list(start_col.range_to(Color(stop_col), 258)) #258 bc we delete first and final elements to make 256
    print("length of hex color list:", len(hex_colors))
    RGB_list = []
    for i in range(1,257): # do this instead of 0,255 to eliminate first and last colors in list - they are a different format.
        curr_col = hex_colors[i]
        curr_col = ImageColor.getcolor(f"{curr_col}", "RGB")
        RGB_list.append(curr_col)
    # print("RGB_ list check", RGB_list)    
    print("length of RGB_list:", len(RGB_list))
    return RGB_list


# Given (x, y) coordinates, return elevation at those coordinates. 
def ele_at_coords(pos, rownum, xy_grid):
    print("line 103", int(xy_grid[rownum][pos]))
    return (xy_grid[rownum][pos])

def ele_to_col_val(min_ele, curr_ele, increment):
    # col_val = int((curr_ele - min_ele)*(1/increment))
    col_val = int(round(curr_ele - min_ele)*(1/increment))
    return col_val  
