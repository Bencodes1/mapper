# mapper
Simple django site that generates an elevation map from a user-submitted latitude,longitude pair

## How it works:
1. User inputs single location (latitude, longitude in decimal form- may add hours/minutes/seconds format later), and scale of area they'd like to measure. 
2. Based on this data, TKTK.py creates grid of GPS coordinates of appropriate size. (Right now the image size doesn't change, and resolution adjusts to scale given. Easy to add a user input toggle of whether they'd like image size to increase with scale.)
3. This grid of coordinates is converted to JSON, and a POST request of this dataset is made using [Open Elevation's API](https://github.com/Jorl17/open-elevation/blob/master/docs/api.md), which returns an elevation (in meters) for each point.
4. This elevation data is extracted and turned into a Raster grid in the TKTK.py file, scaled from the highest elevation to the lowest, and color scaled accordingly.
5. Colored image is rendered with pillow, and displayed in the browser. 

## NOTE:
mapper is under construction... the above steps are for the final version (coming soon!)
