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

