from django.shortcuts import redirect
from .models import *
from django.contrib import messages

def unacthenticated_user(view_func):
    def wrapper_func(request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('store:store')
        else:
            return view_func(request , *args , **kwargs)
    return wrapper_func


def checkout_clarence(view_func):
    def wrapper_func(request , *args , **kwargs):
        order = Order.objects.get(customer=request.user.customer , complete=False)
        items = order.orderitem_set.all()
        flag = True
        if not(order.orderitem_set.exists()):
            flag = False
            messages.info(request, 'unable to proceed, empty cart')
        for i in items:
            if i.height == 1 and i.width == 1:
                flag = False
                messages.info(request, 'your order '+ i.product.name  +' seems odd, you hava ordred 1x1 feet carpet,Idiot donkey view your cart')

        if flag == True:
            return view_func(request , *args , **kwargs)
        else:
            return redirect('store:cart')

    return wrapper_func