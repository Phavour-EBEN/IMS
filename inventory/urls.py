from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.ProductCreateView, name='product-form'),
    path('list/', views.ProductListView, name='product-list'),
    path('update/<int:product_id>/', views.ProductUpdateView, name='product-update'),
    path('delete/<int:product_id>/', views.ProductDelView, name='product-delete'),
]