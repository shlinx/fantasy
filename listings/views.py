from django.views import generic
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
    Listings filter to feed listings based on filters
    """
    def __init__(self, filters=None):
        self.length = 12
        self.filters = filters
        self.listings = TNZListing.objects.all()
        self.filter_listings()
        self.sort_listings()
        self.limit_listings()

    def filter_listings(self):
        """
        Filter listings by criteria from filters.
        :return:
        """
        self.filter_by_types()
        self.filter_by_regions()

    def filter_by_types(self):
        """
        Filter by business types
        :return:
        """
        self.listings = self.listings

    def filter_by_regions(self):
        """
        Filter by regions.
        :return:
        """
        self.listings = self.listings

    def sort_listings(self):
        """
        Sort listings.
        :return:
        """
        self.listings = self.listings

    def limit_listings(self):
        """
        Limit listings.
        :return:
        """
        self.listings = self.listings[: self.length]

    def json(self):
        """
        Serialize the listings result as json format.
        :return:
        """
        return serializers.serialize('json', self.listings)
