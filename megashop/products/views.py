from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, EditProductForm

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

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = EditProductForm(instance=product)
        
    return render(request, 'edit_product.html', {'form': form, 'product':product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('products')
    
    return render(request, 'delete_product.html', {'product':product})
