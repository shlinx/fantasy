from rest_framework import serializers

from listings.models import TNZListing


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TNZListing
        fields = ('name', 'regionname')
