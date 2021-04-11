import csv
import io
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Profile
from .forms import ProductForm, ProfileForm, PositionForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_sold_by
from main.templatetags import product_tags
from django.template.response import TemplateResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


class FormMessageMixin(object):
    @property
    def form_valid_message(self):
        return NotImplemented

    form_invalid_message = 'Please correct the errors below.'

    def form_valid(self, form):
        messages.success(self.request, self.form_valid_message)
        print(self.form_valid_message)
        return super(FormMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.form_invalid_message)
        return super(FormMessageMixin, self).form_invalid(form)


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


class ProductCreateView(FormMessageMixin, CreateView):
    model = Product
    fields = ('__all__')
    success_url = reverse_lazy('home')
    form_valid_message = 'The document was successfully created!'


def is_stock(request):
    # all in stock product list
    products = Product.is_stock.all()
    # sold by currrent user's in stock product list
    sold_by_current_user = Product.is_stock.filter(sold_by=request.user)
    return render(request, 'is_stock.html', {'products': products, 'products_current': sold_by_current_user})


def error_404(request, *args, **kwargs):
    context = {}
    return render(request, 'main/404.html', context)


def error_500(request, *args, **kwargs):
    context = {}
    return render(request, 'main/500.html', context)


def product_image_list(request):
    product = Product.objects.all()
    return render(request, 'product_image_list.html', {'products': product})


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'profile_create.html', {'form': form})


def position_create(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PositionForm()
    return render(request, 'position_create.html', {'form': form})


def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', 'Sold_by', 'Stock'])
    for product in Product.objects.all().values_list('name', 'price', 'sold_by', 'stock'):
        writer.writerow(product)
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    return response


def profile_upload(request):
    prompt = {
        'order': 'Order of the csv should be name, phone_num'
    }
    if request.method == 'GET':
        return render(request, 'profile_upload.html', prompt)

    csv_file = request.FILES['file']
    print(csv_file.name)
    if not csv_file:
        messages.error(request, 'Please choose a file...')
    elif not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    else:
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            obj, created = Profile.objects.update_or_create(
                name=column[0],
                phone_num=column[1],
            )
        return HttpResponse('success')
    return render(request, 'profile_upload.html', {})
