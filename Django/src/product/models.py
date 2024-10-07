from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name
