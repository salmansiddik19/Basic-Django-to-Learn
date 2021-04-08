from django.urls import path
from . import views
from .views import ProductCreateView


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/edit/<int:product_id>/',
         views.product_edit, name='product_edit'),
    path('demo/', views.demo, name='demo'),
    ######################
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
]
