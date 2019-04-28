from django.db import models

# Create your models here.
class Drugs(models.Model):
    name = models.CharField(max_length=250, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=250, blank=True, default='')
    store = models.ManyToManyField('Stores', null=True, blank=True)

    def __str__(self):
        return self.name


class Stores(models.Model):
    name = models.CharField(max_length=250, blank=True, default='')
    street_name = models.CharField(max_length=250, blank=True, default='')
    latitude = models.DecimalField( max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    drug = models.ManyToManyField(Drugs, null=True, blank=True)

    def __str__(self):
        return self.name