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
    booking_email = models.CharField(max_length=50)
    cancellation_policy = models.TextField()
    parking = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True)
    listing_types = ArrayField(models.CharField(max_length=20), null=True)

    tags = models.ManyToManyField(TNZTag)
    main_image = models.OneToOneField(
        TNZImage,
        on_delete=models.CASCADE,
        related_name='main_image_listing',
        null=True,
    )
    logo_image = models.OneToOneField(
        TNZImage,
        on_delete=models.CASCADE,
        related_name='logo_image_listing',
        null=True
    )

    def get_main_image(self):
        try:
            image_instances = next(iter(self.main_image.values()))['instances']
        except (IndexError, AttributeError):
            return {'url': ''}

        try:
            original_image = [instance for instance in image_instances if instance['format'] == 'original'][0]
        except IndexError:
            return {'url': ''}

        return original_image

    def __str__(self):
        return self.name
