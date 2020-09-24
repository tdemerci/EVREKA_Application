from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone


from db.models import NavigationRecord, Vehicle


def read_data(request):
    date_from = datetime.now() - timedelta(days=2)
    q = NavigationRecord.objects.select_related("vehicle").filter(datetime__gt=date_from).values('vehicle__plate', 'datetime', 'latitude', 'longitude').all()
    q2 = NavigationRecord.objects.select_related("vehicle").filter(datetime__gt=date_from).values('vehicle__plate',
                                                                                                 'datetime', 'latitude',
                                                                                                 'longitude').all()
    print(q2.query)
    all_data = list(q)
    max_value_dict = {}
    for element in all_data:
        current_plate = element['vehicle__plate']
        if current_plate not in max_value_dict:
            max_value_dict[current_plate] = element
        elif element['datetime'] >= max_value_dict[current_plate]['datetime']:
            max_value_dict[current_plate] = element
    response = list(max_value_dict.values())
    for element in response:
        element['datetime'] = element['datetime'].strftime("%d.%m.%Y %H:%M:%S")
    return HttpResponse("last points = " + str(response))


def insert_data(request):
    v = Vehicle(plate="00 ABC 99")
    v.save()
    a = NavigationRecord(vehicle=v, datetime=datetime.now(), longitude=33, latitude=44)
    a.save()

    v = Vehicle(plate="12 ABC 99")
    v.save()
    a = NavigationRecord(vehicle=v, datetime=datetime.now(), longitude=33, latitude=44)
    a.save()

    v = Vehicle(plate="00 ABC 99")
    v.save()
    a = NavigationRecord(vehicle=v, datetime=datetime.now(), longitude=33, latitude=44)
    a.save()

    v = Vehicle(plate="01 TAN 97")
    v.save()
    a = NavigationRecord(vehicle=v, datetime=datetime.now(), longitude=33, latitude=44)
    a.save()

    return HttpResponse(str(a.id))
