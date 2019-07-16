from django.shortcuts import render, redirect
from .models import AirportCodes
from .forms import *
import json
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

with open('static/json/airport_codes.json') as json_file:
    airportData = json.load(json_file)
  
def Airport_Code_Index(request):
    if request.method == 'POST':
        user_input = request.POST.get("user_search")
        result = False
        for item in airportData:
            if user_input in item['City']:
                city = item['City']
                code = item['Code']
                context = {
                    'City': city,
                    'Code': code
                }
                result = True               
        if result == True:
            return render(request, 'AirportCodeApp/Airport_Code_Index.html', context)
        else:
            error = {
                'Error': "Sorry, nothing found for that entry. Please try again."
            }
            return render(request, 'AirportCodeApp/Airport_Code_Index.html', error)
    else:
        return render(request, 'AirportCodeApp/Airport_Code_Index.html')

def city_search(request):
    if request.method == 'POST':
        user_input = request.POST.get("user_search")
        result = False
        for item in airportData:
            if user_input in item['Code']:
                city = item['City']
                code = item['Code']
                context = {
                    'City': city,
                    'Code': code
                }
                result = True               
        if result == True:
            return render(request, 'AirportCodeApp/city_search.html', context)
        else:
            error = {
                'Error': "Sorry, nothing found for that entry. Please try again."
            }
            return render(request, 'AirportCodeApp/city_search.html', error)
    else:
        return render(request, 'AirportCodeApp/city_search.html')

# def code_search(request):
#     if request.method == 'GET':
#         form = CityGetter(request.GET or None)

#         if form.is_valid():
#             selected_city = AirportCodes.objects.City
#             selected_code = AirportCodes.objects.Airport_Code
#             return render(request, 'code_search', {'selected_city': selected_city}, {'selected_code': selected_code})
#         else:
#             all_items = AirportCodes.objects.all
#             return render(request, 'code_search')