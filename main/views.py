from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from main.templatetags import product_tags


def home(request):
    context = {
        'comment': '<p> this is a comment </p>',
        'cycle': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

        # firstof tag
        'var1': None,
        'var2': None,
        'var3': 'this is a firstof value',
        #########################################
        'points': [(1, 2), (4, 7), (6, 9), (8, 11)]
    }
    return render(request, 'index.html', context)


def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'products': product})
