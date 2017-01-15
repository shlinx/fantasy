from django.db import models


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
