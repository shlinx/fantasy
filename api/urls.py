from django.conf.urls import url, include
from rest_framework import routers

from .views import ListingViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'l', ListingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
