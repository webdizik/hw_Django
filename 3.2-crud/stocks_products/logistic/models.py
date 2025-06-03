from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product, related_name='stocks', through='StockProduct')

    def __str__(self):
        return self.address

    
class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, related_name='positions', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='positions', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=1)
