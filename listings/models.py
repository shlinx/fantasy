from django.db import models

# Create your models here.


class RawTag(models.Model):
    """
    Raw dictionary data of Tag
    """
    data = models.TextField()
    name_key = models.CharField(max_length=50)
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.name_key


class RawListing(models.Model):
    """
    Raw dictionary data for Listing
    """
    data = models.TextField()
    unique_id = models.IntegerField()
    name = models.CharField(max_length=200)
