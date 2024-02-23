from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
import stripe
from bag.models import Bag
from .forms import PaymentForm

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)

def checkout(request):
    bag_items = Bag.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in bag_items)

    strpie_public_key = settings.STRIPE_PUBLIC_KEY

    payment_form = PaymentForm()

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
                stripe_payment_method = payment_form.cleaned_data('stripe_payment_method')
                
                if not stripe_payment_method:
                    messages.error(request, 'invalid payment method')
                    return redirect('view_bag')

                intent = stripe.PaymentIntent.create (
                    amount = int(total_price*100),
                    currency= 'usd',
                    description='payment for products',
                    payment_method=stripe_payment_method,
                    confirmation_method='manual',
                    confirm=True,
                    return_url=request.build_absolute_uri(reverse('checkout_success')),
                )

                if intent.status == 'succeeded':
                    messages.success(request, 'payment successful')
                    return redirect('checkout_success')
                else:
                    messages.error((request, 'payment failed'))

    bag_items.delete()

    context = {
        'bag_items': bag_items,
        'total_price': total_price,
        'stripe_public_key': strpie_public_key,
        'payment_form': payment_form,
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request):
     return render(request, 'checkout/checkout_success.html')
