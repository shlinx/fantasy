from django.db import models


class TNZImage(models.Model):
    """
    TNZ Image model. It can have multiple instance with different resolutions and resource urls
    """
    o_id = models.IntegerField()
    unique_id = models.IntegerField()
    type_o_id = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    label = models.TextField()
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    order = models.SmallIntegerField(null=True, blank=True)
    market = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()
    asset_type = models.CharField(max_length=20)
    credit = models.TextField()
    exists = models.BooleanField()
    caption = models.TextField(blank=True)
    url = models.TextField()
    file = models.ImageField(upload_to='listings/', null=True)

    gallery_image_listing = models.ForeignKey(
        'TNZListing',
        on_delete=models.CASCADE,
        related_name='gallery_images',
        null=True
    )



