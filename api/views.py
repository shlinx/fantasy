import json

from django.http import HttpResponse
from django.db.models import Count
from rest_framework import viewsets

from listings.models import TNZListing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = TNZListing.objects.all()
    serializer_class = ListingSerializer


def regions(request):
    """
    Get all the regionname from listings and aggregate listings count.
    :param request:
    :return:
    """
    regions_data = TNZListing.objects.values('regionname').annotate(listings_count=Count('id'))
    response = HttpResponse(json.dumps({'data': list(regions_data)}))
    response.__setitem__('Content-Type', 'application/json')
    return response


def types(request):
    """
    Get all the business types from listings and aggregate listings count.
    :param request:
    :return:
    """
    types_data = TNZListing.objects.values('business_type').annotate(listings_count=Count('id'))
    response = HttpResponse(json.dumps({'data': list(types_data)}))
    response.__setitem__('Content-Type', 'application/json')
    return response
