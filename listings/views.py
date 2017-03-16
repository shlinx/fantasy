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
        self.filters = self.sanitize_filters(filters)
        self.listings = TNZListing.objects.all()
        self.filter_listings()
        self.sort_listings()
        self.limit_listings()

    @staticmethod
    def sanitize_filters(raw_filters):
        """
        Sanitize filters from raw filters data.
        :param raw_filters:
        :return:
        """
        effective_filters = {}
        if not isinstance(raw_filters, dict):
            return effective_filters

        # Sanitize keyword
        if 'k' in raw_filters and isinstance(raw_filters['k'], str):
            effective_filters['keyword'] = raw_filters['k']

        # Function to filter data that can be list
        def sanitize_list_filter(data):
            if isinstance(data, str):
                return [data]
            elif isinstance(data, list) and len(data) > 0:
                effective_data = []
                for item in data:
                    if isinstance(item, str):
                        effective_data.append(item)
                return effective_data
        # Sanitize regions
        if 'r' in raw_filters:
            effective_filters['regions'] = sanitize_list_filter(raw_filters['r'])
        # Sanitize types
        if 't' in raw_filters:
            effective_filters['types'] = sanitize_list_filter(raw_filters['t'])

        return effective_filters

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