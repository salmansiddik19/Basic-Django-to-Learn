from django.urls import path
from . import views
from .views import ProductCreateView


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/images/', views.product_image_list, name='product_image_list'),
    path('products/edit/<int:product_id>/',
         views.product_edit, name='product_edit'),
    path('products/stock-list/',
         views.is_stock, name='is_stock'),
    path('products/export/', views.export, name='export'),
    path('demo/', views.demo, name='demo'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/upload/', views.profile_upload, name='profile_upload'),
    path('position/create/', views.position_create, name='position_create'),

    ##########  class based view ############
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
]
