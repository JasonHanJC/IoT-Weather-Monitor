# Box 8.12: Example of a Django view

from django.shortcuts import render_to_response
from weatherStation.models import *
from django.template import RequestContext

def home(request):
    tempData = TemperatureData.objects.order_by('-id')[0]
    temperature = tempData.temperature
    lat = tempData.lat
    lon = tempData.lon

    return render_to_response('index.html', {'temperature':temperature,
    'lat': lat, 'lon': lon}, context_instance=RequestContext(request))