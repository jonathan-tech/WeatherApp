from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
#af5b7e6f7bfea30b47ccac1ef034a00e api key
# Create your views here.
def index(request):
    #the url form the website, use the api key and paste it to the end. units as imperial to get regular degrees
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=af5b7e6f7bfea30b47ccac1ef034a00e'


    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    #prints the info on the commandline
    weather_data=[]

    #print(response.text)
    cities=City.objects.all()
    for city in cities:
        #the infor for the city json will convert it to dictionarys
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
    context = {'weather_data':weather_data, 'form':form}
    #to the template
    return render(request,'weather/weather.html',context)
