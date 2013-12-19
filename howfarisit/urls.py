from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'show_distance', name='show_distance'),
)
