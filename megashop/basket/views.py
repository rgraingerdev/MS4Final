from django.shortcuts import render, get_object_or_404, redirect
from .models import BasketItem
from products.models import Product
from .forms import AddToBasketForm


def basket(request):
    basket_items = BasketItem.objects.filter(user=request.user)

    for item in basket_items:
        item.total_price = item.quantity * item.product.price

    total_cost = sum(item.total_price for item in basket_items)
    total_products = sum(item.quantity for item in basket_items)

    return render(request, 'basket.html', {'basket_items': basket_items, 'total_cost':total_cost, 'total_products': total_products})

def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            basket_item, created = BasketItem.objects.get_or_create(
                user=request.user,
                product=product
            )
            if not created:
                basket_item.quantity += quantity
                basket_item.save()
            return redirect('products')
    else:
        form = AddToBasketForm(initial={'product_id': product_id})
    
    return render(request, 'add_to_basket.html', {'form': form, 'product':product})

def clear_basket(request):
    BasketItem.objects.filter(user=request.user).delete()
    return redirect('basket')
