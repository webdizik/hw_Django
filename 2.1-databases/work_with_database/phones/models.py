from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.URLField()
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField(allow_unicode=True, unique=True)
