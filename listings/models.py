import ast
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class TNZTag(models.Model):
    """
    TNZ Tag model
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
        all_listings = TNZListing.objects.filter(market='cn')
        return [listing for listing in all_listings if listing.regionname() == self.label]


class TNZListing(models.Model):
    """
    TNZ Listing model
    """
    name = models.CharField(max_length=200)
    main_image = JSONField(null=True, blank=True)
    logo_image = JSONField(null=True, blank=True)
    gallery_images = JSONField(null=True, blank=True)
    """
    Original fields
    """
    unique_id = models.IntegerField()
    market = models.CharField(max_length=5)
    modified_date = models.DateTimeField()
    listing_description = models.TextField()
    listing_summary = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    regionname = models.CharField(max_length=50)
    business_type = models.CharField(max_length=200)
    minimum_age = models.SmallIntegerField()
    max_capacity = models.TextField()
    website_link = models.TextField()
    booking_link = models.TextField()
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField()
    operational_hours = models.TextField()
    street = models.TextField()
    suburb = models.TextField()
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    proximity_to_town = models.TextField()
    proximity_to_airport = models.TextField()
    freephone = models.CharField(max_length=50)
    tags = JSONField()
    listing_types = JSONField()
    booking_email = models.CharField(max_length=50)
    cancellation_policy = models.TextField()
    parking = models.TextField()

    def __str__(self):
        return self.name
