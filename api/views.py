from django.http import HttpResponse

from listings.views import ListingsFilter


def listings(request):
    response = ListingsFilter(request.GET)
    return HttpResponse('Hello')
