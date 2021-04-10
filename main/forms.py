from PIL import Image
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')

    def save(self, *args, **kwargs):
        product = super().save(*args, **kwargs)

        x = 5    # self.cleaned_data.get('x')
        y = 5    # self.cleaned_data.get('y')
        w = 10   # self.cleaned_data.get('width')
        h = 10   # self.cleaned_data.get('height')

        image = Image.open(product.image)
        # cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = image.resize((300, 200), Image.ANTIALIAS)
        # image.thumbnail((300, 300))
        resized_image.save(product.image.path)
        # image.save(product.image.path)

        return product
