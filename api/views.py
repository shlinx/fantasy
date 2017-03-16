import json

from django.http import HttpResponse
from django.core.serializers import serialize
from django.db.models import Count

from listings.views import ListingsFilter
from listings.models import TNZListing


def listings(request):
    """
    The listings api json feed.
    :param request:
    :return:
    """
    body = ListingsFilter(request.GET).json()
    response = HttpResponse(body)
    response.__setitem__('Content-Type', 'application/json')
    return response


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
