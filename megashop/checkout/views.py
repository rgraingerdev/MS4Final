from django.shortcuts import render, redirect, get_object_or_404
import stripe
from .forms import PaymentForm
from basket.models import BasketItem
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    basket_item = BasketItem.objects.filter(user=request.user)
    total_cost = sum(item.quantity * item.product.price for item in basket_item)

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            token = form.cleaned_data['stripeToken']
            charge = stripe.Charge.create (
                amount=int(total_cost * 100),
                currency='gbp',
                description=f'Payment for {basket_item.quantity} x {basket_item.product.name} in {basket_item.user.username}\'s Basket',
                source=token
            )

            return redirect('products')
    else:
        form = PaymentForm()
    
    return render(request, 'checkout.html', {'form':form, 'basket_item':basket_item, 'total_cost': total_cost})

# Create your views here.
