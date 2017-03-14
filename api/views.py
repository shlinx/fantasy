from django.http import HttpResponse

from listings.views import ListingsFilter


def listings(request):
    """
    The listings api json feed.
    :param request:
    :return:
    """
    body = ListingsFilter(sanitize_filters(request.GET)).json()
    response = HttpResponse(body)
    response.__setitem__('Content-Type', 'application/json')
    return response


def sanitize_filters(raw_filters):
    """
    Sanitize filters from raw filters data.
    :param raw_filters:
    :return:
    """
    return raw_filters
