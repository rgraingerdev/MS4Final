from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    product = get_object_or_404(Product, id=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = AddToBagForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity', 1)

            bag_items = Bag.objects.filter(user=request.user, product=product)

            if bag_items.exists():
                bag_item = bag_items.first()
                bag_item.quantity += quantity
                bag_item.save()
            else:
                bag_item = Bag.objects.create(
                    user=request.user,
                    product=product,
                    quantity=quantity
                )

            return redirect('products')
    
    form = AddToBagForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'bag/add_to_bag.html', context)

    

def adjust_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)