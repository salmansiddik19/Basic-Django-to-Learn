from django.test import TestCase
from .models import Product


class BasicTest(TestCase):
    def test_fields(self):
        product = Product()
        product.name = 'test item'
        product.description = 'it is a test item'
        product.price = 999
        product.save()

        record = Product.objects.get(pk=1)
        self.assertEqual(record, product)

    def test_slug_on_save(self):
        product = Product()
        product.name = 'test item'
        product.description = 'it is a test item'
        product.price = 999
        product.save()

        self.assertEqual(product.stock, False)
