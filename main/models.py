from django.db import models
from django.contrib.auth.models import User


class CustomProductManager(models.Manager):
    def get_queryset(self):
        return super(CustomProductManager, self).get_queryset().filter(stock=True)


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    stock = models.BooleanField(default=False)

    objects = models.Manager()
    is_stock = CustomProductManager()

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.CharField(max_length=100)
    reviewed_on = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
