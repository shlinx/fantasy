from django.db import models

# Create your models here.


class TNZTag(models.Model):
    """
    Raw dictionary data of Tag
    """
    unique_id = models.IntegerField()
    o_id = models.IntegerField()
    label = models.CharField(max_length=200)
    listing_count = models.IntegerField()
    name_key = models.CharField(max_length=200)
    market = models.CharField(max_length=5)

    def __str__(self):
        return self.name_key


class TNZRegion(models.Model):
    unique_id = models.IntegerField()
    o_id = models.IntegerField()
    label = models.CharField(max_length=200)
    name_key = models.CharField(max_length=50)
    market = models.CharField(max_length=5)

    def __str__(self):
        return self.label


class TNZRawListing(models.Model):
    """
    Raw dictionary data for Listing
    """
    unique_id = models.IntegerField()
    name = models.CharField(max_length=200)
    market = models.CharField(max_length=5)
    data = models.TextField()

    def __str__(self):
        return self.name
