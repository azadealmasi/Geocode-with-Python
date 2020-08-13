
from geopy.geocoders import Nominatim
import pandas as pd
import gmplot
import numpy as np
import webbrowser
df = pd.read_csv("addresses.csv")
locator = Nominatim(user_agent="myGeocoder")
latitude=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
longitude=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
for x in df["addess"]:
  location = locator.geocode(x)
  latitude[i] = location.latitude
  longitude[i] = location.longitude
  i+=1
  print((location.latitude, location.longitude))

gmap = gmplot.GoogleMapPlotter(0, 0, 2)
gmap.heatmap(latitude, longitude)
gmap.scatter(latitude, longitude, c='r', marker=True)
gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
gmap.draw("map.html")
webbrowser.open_new_tab("map.html")
