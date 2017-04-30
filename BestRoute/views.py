import json
import sys
import geocoder
from pickle import dump, load
import Ellipse
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from BestRoute.models import CrimeDataPoint
from Map_Quest_Get import Send_Data
from django.core.management import execute_from_command_line
from routehome.settings import GoogleMaps_API, MapQuest_API

# import panda or google maps api here after you pip install it
# do not forget to add it to INSTALLED_APPS in RouteHome.settings


# Renders out the inital HTML form for user input
# The form is a GET form so all params will be passed through the url
# When the form is submited the params are then passed into the next url
# '/map' which calls the crime map view
def location_form(request):
    return render(request, 'pages/location-form.html')

# This view serves to render out the google map and process all the
# queries from our DB


def crime_map(request):
    # Takes in URL params passed from locataion_form
    location_a = request.GET.get('location_a', '')
    location_b = request.GET.get('location_b', '')
    filters = {
        'homicide': 'Homicide',
        'caraccident': 'Vehicle Accident',
        'oui': 'Operating Under the Influence',
        'indecentAssault': 'Indecent Assault',
        'kidnap': 'Missing Person',
        'robbery': 'Robbery',
        'autotheft': 'Auto Theft',
        'larceny': 'Larceny',
        'burglary': 'Burglary',
        'conduct': 'Disorderly Conduct',
        'disputes': 'Verbal Disputes',
        'prostitution': 'Prostitution',
        'sexoffender': 'Sex Offender'
    }

    final_crime_array = []
    all_crimes = CrimeDataPoint.objects.all()

    for (key, value) in filters.items():
        name = request.GET.get(key, False)
        if name:
            final_crime_array.extend(all_crimes.filter(offense_code_group__icontains=value))

    # if kidnap:
    #     final_crime_array.extend(all_crimes.filter(offense_code__gte=2001).filter(offense_code__lte=3000))

    locA = geocoder.google(location_a)
    locB = geocoder.google(location_b)
    latlongA = locA.latlng
    latlongB = locB.latlng
    ell = Ellipse.Ellipse(latlongA[0], latlongA[1], latlongB[0], latlongB[1])
    jsonObject = {}
    jsonObject['routeControlPointCollection'] = []
    for crime in final_crime_array:
        if not crime.latitude or crime.longitude:
            continue
        if ell.isWithinEllipse(crime.latitude, crime.longitude):
            print(True)
            json_entry = {
                'lat': crime.latitude,
                'long': crime.longitude,
                'weight': 5,
                'radius': 2
            }
            jsonObject['routeControlPointCollection'].append(json_entry)
        else:
            print(False)

    map_quest_api = Send_Data(location_a, location_b, jsonObject)

    try:
        route = map_quest_api.Get_Directions()['route']['legs'][0]['maneuvers']
    except:
        return redirect('/')

    print(GoogleMaps_API)
    context = {
        'location_a': location_a,
        'location_b': location_b,
        'route': route,
        'googleAPI': GoogleMaps_API
    }
    # This renders our the crime-map.html file with all of the defined context
    # variables
    return render(request, 'pages/crime-map.html', context)
