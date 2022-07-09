import email
from django.db import models

class inputs(models.Model):
    time = models.CharField(max_length=2)
    uid = models.TextField(max_length=100)
    destination = models.TextField(max_length=15)

