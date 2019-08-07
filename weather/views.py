from django.shortcuts import render
import requests
from .models import City
#af5b7e6f7bfea30b47ccac1ef034a00e api key
# Create your views here.
def index(request):
    #the url form the websit
    url= 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    #this what we will pass in
    city="london"
    #prints the info on the commandline
    weather_data=[]
    #print(response.text)
    cities=City.objects.all()
    for city in cities:
        #the infor for the city
        r= requests.get(url.format(city)).json()
        #the specific infor that we want to extract from the api
        city_weather = {
            'city': city.name ,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'] ,
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    #we want to place thls infor to the interface
    context = {'weather_data':weather_data}
    #to the template
    return render(request,'weather/weather.html',context)
