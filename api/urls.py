from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from . import views
from listings.models import TNZListing

app_name = 'api'


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TNZListing
        fields = ('name', 'regionname')


class ListingViewSet(viewsets.ModelViewSet):
    queryset = TNZListing.objects.all()
    serializer_class = ListingSerializer

router = routers.DefaultRouter()
router.register(r'l', ListingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
