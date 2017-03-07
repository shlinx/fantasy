from django.db import models
from django.utils import timezone


class ContactRecord(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
