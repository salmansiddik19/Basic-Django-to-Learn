from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .models import Product


def user_is_sold_by(function):
    def wrap(request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['product_id'])
        if product.sold_by == request.user:
            return function(request, *args, **kwargs)
        else:
            return HttpResponse('You are not the right user to edit!')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
