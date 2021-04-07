from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_sold_by
from main.templatetags import product_tags
from django.template.response import TemplateResponse
from django.contrib import messages


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


@login_required
@user_is_sold_by
def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None,
                       request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product_edit.html', {'form': form})


def demo(request):
    context = {}
    return TemplateResponse(request, 'demo.html', context=context)
