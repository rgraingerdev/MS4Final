from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products' : products})

def add_product(request):
    if request.method== 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})