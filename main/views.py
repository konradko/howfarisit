from django.shortcuts import render

from main.models import Distance

def view_distance(request):
    user_distance = Distance(
        user_ip='ip',
        user_location='loc',
        dest_location='dest_loc',
        distance='dummy distance'
        )
    return render(
        request,
        'distance.html',
        {'distance': user_distance}
    )