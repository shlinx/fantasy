from django.views import generic
from listings.models import TNZListing


class Index(generic.ListView):
    template_name = 'listings/index.html'
    model = TNZListing
