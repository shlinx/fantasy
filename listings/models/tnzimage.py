from django.db import models


class TNZImage(models.Model):
    """
    TNZ Image model. It can have multiple instance with different resolutions and resource urls
    """
    o_id = models.IntegerField()
    unique_id = models.IntegerField()
    type_o_id = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    label = models.CharField(max_length=200)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    order = models.SmallIntegerField(null=True, blank=True)
    market = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()
    asset_type = models.CharField(max_length=20)
    credit = models.CharField(max_length=200)
    exists = models.BooleanField()
    caption = models.CharField(max_length=200)
    url = models.TextField()

    gallery_image_listing = models.ForeignKey(
        'TNZListing',
        on_delete=models.CASCADE,
        related_name='gallery_images',
        null=True
    )


class TNZImageInstance(models.Model):
    """
    The actual instance model for TNZImage
    """
    provider_label = models.CharField(max_length=50)
    format = models.CharField(max_length=20)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    url = models.TextField()

    image = models.ForeignKey(
        TNZImage,
        on_delete=models.CASCADE,
        related_name='instances',
    )



