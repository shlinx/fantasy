from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

from listings.models import TNZListing


class HomePage(Page):
    listings = TNZListing.objects.all()[:12]
