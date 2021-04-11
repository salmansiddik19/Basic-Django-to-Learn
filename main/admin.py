from django.contrib import admin
from .models import Product, Review, Profile, PointOfInterest
from simple_history.admin import SimpleHistoryAdmin


class ProductHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["name", "sold_by", 'price', 'stock']
    history_list_display = ["stock"]
    search_fields = ['name', 'user__username']


admin.site.register(Product, ProductHistoryAdmin)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(PointOfInterest)
