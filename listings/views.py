from django.shortcuts import render
from django.views import generic

from .models import TNZRegion

# Create your views here.


class Index(generic.ListView):
    template_name = 'listings/index.html'
    model = TNZRegion


class Region(generic.DetailView):
    template_name = 'listings/region.html'
    model = TNZRegion
