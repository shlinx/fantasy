from django.shortcuts import render
from django.views import generic

from .models import TNZRegion
from .models import TNZListing

# Create your views here.


class Index(generic.ListView):
    template_name = 'listings/index.html'
    model = TNZListing


class Region(generic.DetailView):
    template_name = 'listings/region.html'
    model = TNZRegion

class Listing(generic.DeleteView):
    template_name = 'listings/listing.html'
    model = TNZListing

