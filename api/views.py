import json

from django.http import HttpResponse
from django.db.models import Count
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from listings.models import TNZListing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    The list of listings which is filtered by different criteria.
    """
    queryset = TNZListing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('regionname', 'business_type')
    search_fields = ('name', 'listing_summary', 'regionname', 'business_type')
    ordering_fields = ('name', 'regionname'),
    ordering = ('name',)


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
