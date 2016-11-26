from django.db import models

# Create your models here.


class TNZTag(models.Model):
    """
    Raw dictionary data of Tag
    """
    name_key = models.CharField(max_length=50)
    o_id = models.IntegerField()
    unique_id = models.IntegerField()
    market = models.CharField(max_length=5)
    label = models.CharField(max_length=50)
    listing_count = models.IntegerField()

    def __str__(self):
        return self.name_key


class TNZRawListing(models.Model):
    """
    Raw dictionary data for Listing
    """
    data = models.TextField()
    unique_id = models.IntegerField()
    name = models.CharField(max_length=200)
