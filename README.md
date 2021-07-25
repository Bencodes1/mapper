# mapper
Simple django site that generates an elevation map from a user-submitted latitude,longitude pair

## How it works:
1. User inputs single location (latitude, longitude in decimal form- may add hours/minutes/seconds format later), and scale of area they'd like to measure, in km. User also decides resolution of square image: right now up to 1024x1024 is supported.  
2. Based on this data, gridmaker.py creates grid of GPS coordinates of appropriate size. 
3. This grid of coordinates is converted to JSON, and a POST request of this dataset is made using [MapQuest's Open Elevation API](https://developer.mapquest.com/documentation/open/elevation-api/), which returns an elevation (in meters) for each point. 
4. This elevation data is extracted and turned into a Raster grid in the rastermaker.py file, scaled from the highest elevation to the lowest, and color scaled accordingly.
5. This image is saved locally- the next step is to host this image online and render it in the browser for the user. 

## NOTE:
This project was initially built with [Open Elevation's API](https://github.com/Jorl17/open-elevation/blob/master/docs/api.md), because its documentation says 'there is no limit' on requests- which is apparently not the case, as I discovered after getting data throttled after making one 1000x1000px image! I have reconfigured it to use mapquest's API, which unfortunately requires a developer key. As a temporary fix, I've required the user to input their own mapquest developer key when making a request. 