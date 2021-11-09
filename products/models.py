from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    craeted_at = models.DateField
    updates_at = models.ForeignKey
