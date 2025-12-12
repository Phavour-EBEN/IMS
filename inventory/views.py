from django.shortcuts import render, redirect
from  .forms import ProductForms
from .models import Product

# Create your views here.

# define the home view
def home(request):
    return render(request, 'inventory/home.html')


# define the CRUD
# define the create view
def ProductCreateView(request):
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    context = {'form':form}
    return render(request, 'inventory/product-form.html', context)

# define the read product list view
def ProductListView(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'inventory/product-list.html', context)


# define the product update view
def ProductUpdateView(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForms()
    if request.method == "POST":
        form = ProductForms(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    
    context = {'form':form}
    return render(request, 'inventory/product-form.html', context)


def ProductDelView(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    context = {"product":product}
    return render(request, 'inventory/product-confirm-del.html', context)