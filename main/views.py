import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.gis.utils import GeoIP
from math import cos, sin, asin, sqrt, radians

from main.models import Distance

# Helper functions
def calc_distance(first_coordinates, second_coordinates):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = first_coordinates
    lon2, lat2 = second_coordinates
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

def get_lon_lat(ip):
    # Use different host for testing, local can't be looked up with GeoIP
    if settings.DEBUG:
        addr = 'google.com'
    else:
        addr = ip
    return GeoIP().lon_lat(addr)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_distance(request):
    user_ip = get_client_ip(request)
    user_coordinates = get_lon_lat(user_ip)
    dest_coordinates = (-0.109762, 51.522199)

    user_distance_obj = Distance(
        user_ip=user_ip,
        distance=calc_distance(
            user_coordinates,
            dest_coordinates
        )
    )
    # Add saving if we want to keep user records
    return user_distance_obj.distance

# Views
def view_distance(request):
    user_distance = get_user_distance(request)
    return render(
        request,
        'distance.html',
        {'distance': user_distance}
    )

def api_view(request):
    user_distance = str(get_user_distance(request))
    response_data = {'Distance': user_distance}
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )