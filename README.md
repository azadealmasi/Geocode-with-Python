# Geocode-with-Python
Convert physical addresses to Geographic locations
# installing
install these libraries with Pip if you have already Anaconda environment setup:
* pip install geopandas
* pip install geopy
# Geocoding Single Address
To geolocate a single address, you can use Geopy python library. Geopy has different Geocoding services that you can choose from, including Google Maps, ArcGIS, AzureMaps, Bing, etc.
As our first example, we use Nominatim Geocoding service, which is built on top of OpenStreetMap data. Let us Geocode a single address, the the Eifel tower in Paris.
```
locator = Nominatim(user_agent=”myGeocoder”)
location = locator.geocode(“Champ de Mars, Paris, France”)
```
We create `locator` that holds the Geocoding service, Nominatim. Then we pass the locator we created to geocode any address, in this example, the Eifel tower address.
```
print(“Latitude = {}, Longitude = {}”.format(location.latitude, location.longitude))
```
Now, we can print out the coordinates of the location we have created.
```
Latitude = 48.85614465, Longitude = 2.29782039332223
```

# Geocoding List Address
# Show physical addresses in Google Map





