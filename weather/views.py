from django.shortcuts import render,redirect
from .models import Cities
import requests
# Create your views here.
def index(request):
    cities = Cities.objects.all()
    context = {
        'cities' : cities
    }
    return render(request,'weather/index.html',context)
def add(request):
    if request.method == 'POST':
        city = request.POST['cityname']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=10ea308a7f68ad5ddbd38dd4a7e47cce'
        r = requests.get(url.format(city)).json()
        description = r['weather'][0]['description']
        temperature = r['main']['temp']
        city = Cities(city = city,temperature = temperature,description = description)
        city.save()
        return redirect('/')
    else:
        return render(request,'weather/index.html')    
def delete(request,id):
    city = Cities.objects.filter(pk = id)
    city.delete()
    return redirect('/')        
        