import csv

from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator

from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as file_csv:
        reader = csv.DictReader(file_csv)
        bus_stations_list = [row for row in reader]

def bus_stations(request):
    p = Paginator(bus_stations_list, 10)
    current_page = int(request.GET.get('page', 1))
    page = p.get_page(current_page)
    
    context = {  
        'page': page,         
        'bus_stations': page.object_list,
    }
    
    return render(request, 'stations/index.html', context)
