from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
import requests

def get_map_tile(request, z, x, y):
    api_key = config('API_KEY')  # Your hidden API key
    tile_url = f"https://tiles.waqi.info/tiles/usepa-aqi/{z}/{x}/{y}.png?token={api_key}"
    response = requests.get(tile_url)
    return HttpResponse(response.content, content_type=response.headers['Content-Type'])
    
def get_air_quality(api_key, city_name):
    url = f"http://api.waqi.info/feed/{city_name}/?token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            # Current air quality data
            filtered_data = {
                'aqi': data.get('aqi'),
                'time': data.get('time', {}).get('s'),
                'pm25': data.get('iaqi', {}).get('pm25', {}).get('v', 'Not available'),
                'pm10': data.get('iaqi', {}).get('pm10', {}).get('v', 'Not available'),
                'no2': data.get('iaqi', {}).get('no2', {}).get('v', 'Not available'), 
                'co': data.get('iaqi', {}).get('co', {}).get('v', 'Not available'),
                'so2': data.get('iaqi', {}).get('so2', {}).get('v', 'Not available'),
                'o3': data.get('iaqi', {}).get('o3', {}).get('v', 'Not available')
            }
            # Extract forecast data
            forecast_data = data.get('forecast', {}).get('daily', {})
            filtered_data['forecast'] = forecast_data

            return filtered_data
        else:
            return {"error": "No data available"}
    else:
        return {"error": "API request failed"}


def recommend_outdoor_activity_days(forecast_data, safe_threshold=50):
    safe_days = []
    
    for forecast in forecast_data:
        if forecast['avg'] < safe_threshold:
            safe_days.append(forecast['day'])
    
    return safe_days


def get_city_coordinates(city_name, api_key):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {'q': city_name, 'key': api_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            coordinates = data['results'][0]['geometry']
            lat = float(coordinates['lat'])  # Ensure latitude is a float
            lng = float(coordinates['lng'])  # Ensure longitude is a float
            return lat, lng
        else:
            return None, None  # No coordinates found
    else:
        return None, None  # API request failed

def index(request):
    API_KEY = config('API_KEY')
    API_KEY2 = config('API_KEY2')
    # Get city from the query parameters
    city = request.GET.get('city')

    if city:
        air_quality_data = get_air_quality(API_KEY, city)
        latitude, longitude = get_city_coordinates(city, API_KEY2)

        if 'error' not in air_quality_data:
            forecast_data = air_quality_data.get('forecast', {}).get('pm25', [])
            safe_days = recommend_outdoor_activity_days(forecast_data)

            context = {
                'city': city,
                'latitude': latitude,
                'longitude': longitude,
                'air_quality_data': air_quality_data,
                'safe_days': safe_days
            }
        else:
            context = {
                'city': city,
                'error': air_quality_data['error']
            }
    else:
        # No city provided, prepare a default context
        context = {'message': 'Please enter a city to get air quality information.'}

    return render(request, 'air_app/index.html', context)






