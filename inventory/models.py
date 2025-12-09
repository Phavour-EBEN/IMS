from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} : {self.quantity}"