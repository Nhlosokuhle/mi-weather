from django.shortcuts import render
from datetime import datetime
import requests

# Create your views here.
def index(request):
    """
    View function that renders the index.html template with the current weather and datetime.
    
    :param request: the HTTP request object
    :type request: django.http.HttpRequest
    :return: an HTTP response with the rendered index.html template
    :rtype: django.http.HttpResponse
    """
    now = datetime.now() # get the current datetime
    if request.method == "POST": # check if the request is a POST request
        city = request.POST.get("city") # get the city from the POST data
        weather = get_weather(city) # get the weather for the city using the get_weather function
    else:
        weather = None # if it's not a POST request, set weather to None
    return render(request, "index.html", {"weather": weather, 'now': now}) # render the index.html template with the weather and datetime as context variables

def get_weather(city):
    """
    Get the weather data for a given city using the OpenWeatherMap API.

    :param city: the name of the city to get the weather data for
    :type city: str
    :return: a dictionary containing various weather information for the city
    :rtype: dict
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "2f7d18c29e11ed1ca0ed50ed3d0eab9f",
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()
    data = response.json()
    city = data["name"]
    temperature = round(data['main']['temp'])
    description = data['weather'][0]['description'].title()
    icon_code = data['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'
    min_temperature = data["main"]["temp_min"]
    max_temperature = data["main"]["temp_max"]
    real_feel = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    weather = {
        "city": city,
        "temperature": temperature,
        'description': description,
        'icon': icon_url,
        "min_temperature": min_temperature,
        "max_temperature": max_temperature,
        "real_feel": real_feel,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "pressure": pressure
    }
    return weather
