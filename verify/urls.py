from django.conf.urls import patterns, url
from verify import views
from treadStone import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^retrieve', views.retrieve, name = 'retrieve'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
)
