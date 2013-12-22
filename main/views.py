import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError

from tools import get_user_distance

def view_distance(request):
    """
    Renders template with user location or error message
    """
    user_distance = get_user_distance(request)
    if user_distance:
        content = "%i km" % user_distance
    else:
        content = "Sorry, can't get your location."
    return render(
        request,
        'base.html',
        {'content': content}
    )

def api_view(request):
    """
    Responds with user location in JSON format or error message
    """
    user_distance = get_user_distance(request)
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