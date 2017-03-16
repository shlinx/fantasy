from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^l/$', views.listings, name='listings'),
    url(r'^r/$', views.regions, name='regions'),
    url(r'^t/$', views.types, name='types'),
]
