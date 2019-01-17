from django.shortcuts import render, get_object_or_404
from .models import Product
# CART stuff
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import json


def index(request):
    context = {
        'products': Product.objects.all(),
        'bests': Product.objects.order_by('id').filter(best=True),
        'laptops': Product.objects.order_by('id').filter(category=1)[:4],
        'headsets': Product.objects.order_by('id').filter(category=2)[:4],
    }
    return render(request, 'store/index.html', context)


def product(request, slug):
    context = {
        'product': get_object_or_404(Product, slug=slug)
    }
    return render(request, 'store/product.html', context)


def search(request):
    products = Product.objects.all()
    q = request.GET['q']
    cat = request.GET['cat']

    if cat and cat != '':
        products = Product.objects.filter(category=cat)
    if q:
        products = Product.objects.filter(details__icontains=q)

    context = {
        'products': products
    }
    return render(request, 'store/search.html', context)


def cart(request):
    return render(request, 'store/cart.html')


@csrf_exempt
def get_cart_items(request):
    if request.method == 'POST':
        products = json.loads(request.POST['products'])
        items = []

        for product in products:
            items.append(Product.objects.get(pk=int(product)))

        json_items = serializers.serialize('json', items)
        # return json
        return JsonResponse(json_items, safe=False)
