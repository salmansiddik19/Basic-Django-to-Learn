from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField
from simple_history.models import HistoricalRecords
from simple_history import register
from ckeditor.fields import RichTextField


register(User)


class CustomProductManager(models.Manager):
    def get_queryset(self):
        return super(CustomProductManager, self).get_queryset().filter(stock=True)


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(null=True, blank=True)
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    stock = models.BooleanField(default=False)
    history = HistoricalRecords()

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


class Profile(models.Model):
    name = models.CharField(max_length=200)
    phone_num = PhoneNumberField()

    def __str__(self):
        return str(self.phone_num)


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()

    def __str__(self):
        return self.name
