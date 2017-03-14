from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^listings/$', views.listings, name='listings')
]
