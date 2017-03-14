from django.views import generic
from django.http import HttpResponse
from django.core import serializers

from .models import TNZRegion
from .models import TNZListing

# Create your views here.


class Index(generic.ListView):
    template_name = 'listings/listings.html'
    model = TNZListing


class Region(generic.DetailView):
    template_name = 'listings/region.html'
    model = TNZRegion


class ListingDetailView(generic.DetailView):
    template_name = 'listings/listing.html'
    model = TNZListing
    context_object_name = 'listing'

    def get_context_data(self, **kwargs):
        context = super(ListingDetailView, self).get_context_data(**kwargs)

        return context


class ListingsFilter:
    """
    The api class to feed listings
    """
    def __init__(self, filters):
        self.filters = filters
        self.listings = TNZListing.objects.all()

    def filter_listings(self, request):
        types = request.GET.get('types')
        if len(types) > 0:
            self.filter_by_types(types)

    def filter_by_types(self, types):
        pass

    def get_listings(self):
        return self.listings

    def json(self):
        return serializers.serialize('json', self.listings)
