import googlemaps
from datetime import datetime
import demjson
#address = raw_input("Enter Address:\n")
address = 'hatzlil 5 raanana'
gmaps = googlemaps.Client(key='AIzaSyAgAEI3kSFu9Sb-zUODA7K8sSULjane4qM')
#gmaps = googlemaps.Client(key='Add Your Key here')


# Geocoding an address
geocode_result = gmaps.geocode(address)
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
#                                     mode="transit",
#                                     departure_time=now)
#geocode_result = unicode(geocode_result,'UTF-8')
#decoded = demjson.decode(geocode_result)
#print type(decoded)
#print decoded
print geocode_result
