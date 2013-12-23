# Django app showing distance between approximate visitor location and given destination

Example: <http://howfarissharehoods.korzel.com>

* Calculates the distance with [Haversine Formula](http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
* User geolocation with [GeoIP](https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/)
* Uses [django-ipware](https://pypi.python.org/pypi/django-ipware) to get user ip from request
* /api returns distance in JSON format

## Requirements

[GeoDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/)

## Installation

    git clone https://github.com/konradko/howfarisit.git
    cd howfarisit
    pip install -r requirements.txt
    python manage.py runserver

Visit <http://localhost:8000> or <http://localhost:8000/api> to see it running.

Location cannot be resolved for localhost, so for DEBUG mode 'google.com' is used as user address.

Destination is hard-coded in main/views.py

## Running tests

    python manage.py test main