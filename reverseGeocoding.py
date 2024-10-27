import requests

# Coordinates for the reverse geocode request
def reverse_geocode(latitude, longitude):
    access_token = "pk.eyJ1IjoiamlvdmFuaTEyMyIsImEiOiJjbHl6bWE1Ymkxb2o5MmtzYngxaGJuMWljIn0.olBgfruAbty0QZdtvASqoQ"

    # Mapbox reverse geocode API URL
    url = f"https://api.mapbox.com/search/geocode/v6/reverse?longitude={longitude}&latitude={latitude}&access_token={access_token}"
    response = requests.get(url)
    result = response.json()
    properties = result['features']
    brgy=properties[0]['properties']['context']['locality']['name']
    city=properties[0]['properties']['context']['place']['name']
    province=properties[0]['properties']['context']['region']['name']
    return {"brgy":brgy,"city":city,"province":province}

