from __future__ import absolute_import, unicode_literals
from urllib.parse import urlencode
from django.urls import reverse
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route

from listings.models import TNZListing


class HomePage(RoutablePageMixin, Page):
    listings = TNZListing.objects.all()[:12]

    @route(r'^search/$', name='search')
    def search(self, request):
        """
        Request handler for searching keyword.
        :param request:
        :return:
        """
        query = ''
        keyword = request.POST.get('keyword')
        if keyword:
            query = '?' + urlencode({
                'k': keyword
            })

        return redirect(reverse('search') + query)

    @route(r'^filter/$', name='filter')
    def filter(self, request):
        """
        Request handler for filtering by region and type.
        :param request:
        :return:
        """
        query = ''
        query_data = {}
        has_query = False
        for key, query_key in {'regions': 'r', 'types': 't'}.items():
            value = request.POST.get(key)
            if value:
                query_data[query_key] = value
                has_query = True

        if has_query:
            query = '?' + urlencode(query_data)

        return redirect(reverse('search') + query)

    @staticmethod
    def regions():
        """
        Get all regions.
        :return:
        """
        return TNZListing.all_regions()

    @staticmethod
    def types():
        """
        Get all types.
        :return:
        """
        return TNZListing.all_types()
