from .models import Product


def product_list_renderer(request):
    products = Product.objects.all()
    latest_product = Product.objects.latest('-id')
    context = {
        'product_list': products,
        'latest_product': latest_product,
    }
    return context
