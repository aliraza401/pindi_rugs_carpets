from django.shortcuts import render
from .models import Product, Order

# Create your views here.

def store(request):
    products = Product.objects.all()
    template = 'store/store.html'
    context = {'products':products}

    return render(request, template, context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create( customer=customer, complete=False )
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}

    template = 'store/cart.html'
    context = {
        'items':items,
        'order':order,
    }

    return render(request, template, context)


def checkout (request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create( customer=customer, complete=False )
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}

    template = 'store/checkout.html'
    context = {
        'items':items,
        'order':order,
    }

    return render(request, template, context)