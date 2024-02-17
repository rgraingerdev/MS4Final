from django.shortcuts import render, get_object_or_404, redirect
from .models import BasketItem
from products.models import Product
from .forms import AddToBasketForm


def basket(request):
    basket_items = BasketItem.objects.filter(user=request.user)

    for product in basket_items:
        product.total_price = product.quantity * product.price

    total_cost = sum(total_cost for product in basket_items)

    total_products = sum(total_products for product in basket_items)

    return render(request, 'basket.html', {'basket_items': basket_items, 'total_cost':total_cost})

def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            quantity = 1
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
    
    return render(request, 'add_to_basket.html', {'form': form})
