from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
#af5b7e6f7bfea30b47ccac1ef034a00e api key
# Create your views here.
def index(request):
    #the url form the website, use the api key and paste it to the end. units as imperial to get regular degrees
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=af5b7e6f7bfea30b47ccac1ef034a00e'

    err_msg=''
    #hold message user will see
    message = ''
    #css color message area
    message_class=''

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            #will get the city that exist
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                #the infor for the city json will convert it to dictionarys
                r= requests.get(url.format(new_city)).json()
                #api cod==200 means city has beedn found
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='This city doesnt exist'
            else:
                err_msg="city already on the list"

        if err_msg:
            message= err_msg
            message_class='is-danger'
        else:
            message='City is added successfuly'
            message_class= 'is-success'

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
    context = {
        'weather_data':weather_data,
        'form':form,
        'message': message,
        'message_class':message_class
    }
    #to the template
    return render(request,'weather/weather.html',context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('index')
