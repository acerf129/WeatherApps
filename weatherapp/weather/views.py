from django.shortcuts import render
from datetime import date,datetime
import json
import urllib.request
import ssl
# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city'].upper()
        datarow='datarow'
        ssl._create_default_https_context = ssl._create_unverified_context
        today= date.today()
        now = datetime.now()
        dates = today.strftime("%B %d")
        times= now.strftime("%I:%M %p")
        try:
            res =urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=beedf3a1ced85957c72b8c2a4e06b352').read()
            json_data = json.loads(res)
            data = {
                "country_code":str(json_data['sys']['country']),
                "coordinate":str(json_data['coord']['lon'])+','+
                str(json_data['coord']['lat']),
                "weather_main":str(json_data['weather'][0]['main']),
                "weather_desc":str(json_data['weather'][0]['description']),
                "temp":str(round(float(json_data['main']['temp'])- 273.15,1))+'°C',
                "temp_max":str(round(float(json_data['main']['temp_max'])- 273.15,1))+'°C',
                "temp_min":str(round(float(json_data['main']['temp_min'])- 273.15,1))+'°C',
                "pressure":str(json_data['main']['pressure']),
                "humidity":str(json_data['main']['humidity']),
            }
        except:
            city='Search No Found'
            datarow=''
            data={} 
    else:
        city='TAIWAN'
        datarow='datarow'
        ssl._create_default_https_context = ssl._create_unverified_context
        today= date.today()
        now = datetime.now()
        dates = today.strftime("%B %d")
        times= now.strftime("%I:%M %p")
        try:
            res =urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=beedf3a1ced85957c72b8c2a4e06b352').read()
            json_data = json.loads(res)
            data = {
                "country_code":str(json_data['sys']['country']),
                "coordinate":str(json_data['coord']['lon'])+','+
                str(json_data['coord']['lat']),
                "weather_main":str(json_data['weather'][0]['main']),
                "weather_desc":str(json_data['weather'][0]['description']),
                "temp":str(round(float(json_data['main']['temp'])- 273.15,1))+'°C',
                "temp_max":str(round(float(json_data['main']['temp_max'])- 273.15,1))+'°C',
                "temp_min":str(round(float(json_data['main']['temp_min'])- 273.15,1))+'°C',
                "pressure":str(json_data['main']['pressure']),
                "humidity":str(json_data['main']['humidity']),
            }
        except:
            city='Search No Found'
            datarow=''
            data={} 
    return render(request,'index.html', {'city':city, "data":data,'datarow':datarow,'dates':dates,'times':times}) 