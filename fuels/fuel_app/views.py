from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from fuel_app.models import Fuel_price
from django.core.serializers import serialize
# Create your views here.
def Get_Price(request):
     # Retrieve all records and order them by 'city_name'
    records = Fuel_price.objects.all().order_by('city_name')
    serialized_data=serialize("json",records)
    print(serialized_data)
    # Convert JSON string to Python list/dictionary
    data = json.loads(serialized_data)
    print(data)
    return HttpResponse(("thid is id"))

@csrf_exempt
def Put_Price(request):
    form_data = json.loads(request.body)
    # print(form_data)
    for data in form_data:
        city=data
        petrol_price=form_data[city][0]
        diesel_price=form_data[city][0]
        # Try to get the existing record based on the unique identifier (city)
        obj, created = Fuel_price.objects.get_or_create(city_name=city, defaults={
            'petrol_price': petrol_price,
            'diesel_price': diesel_price,
        })
        # If the record was not created, update the prices
        if not created:
            obj.petrol_price = petrol_price
            obj.diesel_price = diesel_price
            obj.save()
    print("successfully inserted record")    
        