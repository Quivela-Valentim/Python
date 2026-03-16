from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="meu_codigo")
endereco = geolocator.geocode("Luanda, Angola")

print(endereco.address)
print(endereco.latitude, endereco.longitude)

