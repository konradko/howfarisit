from django.conf.urls import patterns, url

import main.views

urlpatterns = patterns('',
    url(r'^$', main.views.view_distance, name='view_distance'),
)
