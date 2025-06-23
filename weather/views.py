from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponse
from dotenv import load_dotenv
import os

load_dotenv()
 
api_key = os.getenv('OPENWEATHER_API_KEY')
# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+ '&units=metric&appid='+ api_key).read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) +'°C',
                "description": str(json_data['weather'][0]['main']),
                "pressure": str(json_data['main']['pressure']) + 'hPa',
                "humidity": str(json_data['main']['humidity']) + '%',

            }
        else:   
            city = ''
            data = ''
    except Exception as e:
        return HttpResponse(str(e))
    return render(request, 'index.html', {'city':city, 'data': data})