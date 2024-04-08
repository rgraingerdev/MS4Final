from django.shortcuts import render, redirect, HttpResponse,
    get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib import messages
from .forms import AddToBagForm
from .models import Bag
from profiles.models import UserProfile
from products.models import Product

# Create your views here.


def view_bag(request):
    bag_items = Bag.objects.all()
    bag_items_count = bag_items.count()
    bag_total = sum(item.total_price for item in bag_items)

    context = {
        'bag_items': bag_items,
        'bag_items_count': bag_items_count,
        'bag_total': bag_total,
}
    return render(request, 'bag/bag.html', context)


@login_required
def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    user = get_object_or_404(UserProfile, user = request.user)

    if request.method == 'POST':
        form = AddToBagForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST.get('quantity', 1))

            bag_items = Bag.objects.filter(
                user = request.user, product = product
             )

            if bag_items.exists():
                bag_item = bag_items.first()
                bag_item.quantity += quantity
                bag_item.save()
            else:
                bag_item = Bag.objects.create(
                    user = request.user,
                    product = product,
                    quantity = quantity
                 )

            return redirect('products')
 
    form = AddToBagForm()
    context = {
        'product': product,
        'form': form,
}
    return render(request, 'bag/add_to_bag.html', context)


def remove_from_bag(request, product_id):

        bag_item = Bag.objects.get(user = request.user, id = product_id)
        bag_item.delete()
        messages.success(request, 'item removed from bag')
        return redirect('view_bag')
