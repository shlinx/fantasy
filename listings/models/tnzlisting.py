from django.db import models
from django.contrib.postgres.fields import ArrayField

from .tnztag import TNZTag
from .tnzimage import TNZImage


class TNZListing(models.Model):
    """
    TNZ Listing model
    """
    name = models.CharField(max_length=200)
    """
    Original fields
    """
    unique_id = models.IntegerField()
    market = models.CharField(max_length=5)
    modified_date = models.DateTimeField(null=True)
    listing_description = models.TextField()
    listing_summary = models.TextField()
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    regionname = models.CharField(max_length=50)
    business_type = models.CharField(max_length=200)
    minimum_age = models.SmallIntegerField(null=True)
    max_capacity = models.TextField()
    website_link = models.TextField()
    booking_link = models.TextField()
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    operational_hours = models.TextField()
    street = models.TextField()
    suburb = models.TextField()
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    proximity_to_town = models.TextField()
    proximity_to_airport = models.TextField()
    freephone = models.CharField(max_length=50)
    booking_email = models.CharField(max_length=50)
    cancellation_policy = models.TextField()
    parking = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True)
    listing_types = ArrayField(models.CharField(max_length=20), null=True)

    tags = models.ManyToManyField(
        TNZTag,
        related_name='listings'
    )
    main_image = models.ForeignKey(
        TNZImage,
        on_delete=models.CASCADE,
        related_name='main_image_listing',
        null=True,
    )
    logo_image = models.ForeignKey(
        TNZImage,
        on_delete=models.CASCADE,
        related_name='logo_image_listing',
        null=True,
    )

    def __str__(self):
        return self.name

    def listing_types_string(self):
        return '、 '.join(self.listing_types)

    def address(self):
        return ' '.join((self.street, self.suburb, self.postcode))

    def slider_images(self):
        if self.gallery_images.count():
            return self.gallery_images.all()
        if self.main_image.file:
            return [self.main_image]
        return ()
