from django.shortcuts import render
from django.contrib.gis.utils import GeoIP

from main.models import Distance

# Helper function
def get_user_location(request):
    user_ip = request.META.get('REMOTE_ADDR', None)
    return GeoIP().lon_lat(user_ip)

def view_distance(request):

    user_distance = Distance(
        user_ip='ip',
        user_location='loc',
        dest_location='dest_loc',
        distance=str(get_user_location(request))
        )
    return render(
        request,
        'distance.html',
        {'distance': user_distance}
    )