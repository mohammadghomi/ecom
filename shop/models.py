from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.CharField(max_length=300)
