from django.conf import settings
from django.contrib.gis.utils import GeoIP
from math import cos, sin, asin, sqrt, radians
from ipware.ip import get_ip_address_from_request

# Helper functions
def calc_distance(first_coordinates, second_coordinates):
    """
    Calculates the great circle distance between two points
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

def get_lon_lat(addr):
    """
    Returns (longitude, latitude) tuple for the given address
    """
    # Use different host for testing, local can't be looked up with GeoIP
    if settings.DEBUG:
        addr = 'google.com'
    return GeoIP().lon_lat(addr)

def get_user_coordinates(request):
    user_ip = get_ip_address_from_request(request)
    user_coordinates = get_lon_lat(user_ip)
    return user_coordinates

def get_user_distance(user_coordinates, dest_coordinates):
    """
    Returns approximate user distance from dest_coordinates
    location or None if it can't get user location.
    dest_coordinates must be a (longitude, latitude) tuple.
    """
    user_distance = calc_distance(
        user_coordinates,
        dest_coordinates
    )
    # Add saving if we want to keep user records
    return user_distance