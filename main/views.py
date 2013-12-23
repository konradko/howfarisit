import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError

from tools import get_user_distance

# (longitude, latitude)
destination = (-0.109762, 51.522199)

def view_distance(request):
    """
    Renders template with user location or error message
    """
    user_distance = get_user_distance(request, destination)
    if user_distance:
        content = "%f km" % user_distance
        status_code = 200
    else:
        content = "Sorry, can't get your location."
        status_code = 500
    response = render(
        request,
        'base.html',
        {'content': content}
    )
    response.status_code = status_code
    return response

def api_view(request):
    """
    Responds with user location in JSON format or error message
    """
    user_distance = get_user_distance(request, destination)
    if user_distance:
        response_data = {'Distance': str(user_distance)}
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        response_data = {'Error': "Can't get user location."}
        return HttpResponseServerError(
            json.dumps(response_data),
            content_type="application/json"
        )