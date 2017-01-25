from django.views import generic

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

