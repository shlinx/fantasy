from django.db import models
from .tnzlisting import TNZListing


class TNZRegion(models.Model):
    """
    TNZ Region model
    """
    unique_id = models.IntegerField()
    o_id = models.IntegerField()
    label = models.CharField(max_length=200)
    name_key = models.CharField(max_length=50)
    market = models.CharField(max_length=5)

    def __str__(self):
        return self.label

    def listings(self):
        all_listings = TNZListing.objects.filter(market='cn', regionname=self.label)
        return all_listings
