from django.contrib import admin
from .models import Product, Review, Profile, PointOfInterest


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(PointOfInterest)
