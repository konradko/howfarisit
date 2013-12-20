from django.conf.urls import patterns, url

import main.views

urlpatterns = patterns('',
    url(r'^$', main.views.view_distance, name='view_distance'),
    url(r'^api', main.views.api_view, name='api_view')
)
