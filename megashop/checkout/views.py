from django.shortcuts import render, redirect
import stripe
from .forms import PaymentForm
from products.models import Product
from basket.models import BasketItem
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request, basket_id):
    basket = BasketItem.objects.get(id=basket_id)
    total_price = basket.calculate_total_price()

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            token = form.cleaned_data['stripeToken']
            charge = stripe.Charge.create (
                amount=int(total_price * 100),
                currency='gbp',
                description='Payment for items in the basket',
                source=token
            )

            return redirect('products')
    else:
        form = PaymentForm()
    
    return render(request, 'payment.html', {'form':form, 'basket':basket})

# Create your views here.
