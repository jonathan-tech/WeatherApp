from django.shortcuts import render
import requests
#af5b7e6f7bfea30b47ccac1ef034a00e api key
# Create your views here.
def index(request):
    #the url form the websit
    url= 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
    #this what we will pass in
    city= 'Las Vegas'
    #we are calling the url to get the information from the city city
    r = requests.get(url.format(city)).json()
    #prints the info on the commandline
    #print(response.text)
    #the infor that we want to extract from the api
    city_weather = {
        'city': city ,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'] ,
        'icon': r['weather'][0]['icon'],
    }
    #we want to place thls infor to the interface
    context = {'city_weather':city_weather}
    #to the template
    return render(request,'weather/weather.html',context)
