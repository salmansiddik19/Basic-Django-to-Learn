from django import template
from main.models import Product, Review

register = template.Library()


@register.simple_tag
def calc_review_count(product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(reviewed_on=product)
    return reviews.count()
