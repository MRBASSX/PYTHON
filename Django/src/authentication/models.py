from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.name + ' ' + str(self.price) + ' ' + self.description
