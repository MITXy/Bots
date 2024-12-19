import phonenumbers
from phone import NUMBER, API_KEY
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

prepare = phonenumbers.parse(NUMBER)

location = geocoder.description_for_number(prepare, "en")
provider = carrier.name_for_number(prepare, "en")
print(location, provider)

geocoder = OpenCageGeocode(API_KEY)
query = str(location)
result = geocoder.geocode(query)
print(result)

lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat,lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")