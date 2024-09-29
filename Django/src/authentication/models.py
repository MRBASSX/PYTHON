from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    description = models.TextField(max_length=1000, null=True)
