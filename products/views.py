from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    products_per_page = 9
    paginator = Paginator(products, products_per_page)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'products/products.html', context)
