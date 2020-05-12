<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from .form import HeightWidthForm, CreateCustomerForm, CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import unacthenticated_user, checkout_clarence
from django.contrib import messages

# Create your views here.


def store(request):
    template = 'store/store.html'
    if request.user.is_authenticated:
        products = Product.objects.all()
        customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        products = Product.objects.all()
        customer = ''
        cart_items = ''
    context = {
        'products': products,
        'cart_items': cart_items,
    }
    return render(request, template, context)


@login_required(login_url='store:login')
def view_product(request, id):
    template = 'store/view_product.html'
    product = Product.objects.get(id=id)
    order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
    cart_items = order.get_cart_items
    context = {
        'product': product,
        'cart_items': cart_items,
    }
    return render(request, template, context)


@login_required(login_url='store:login')
def cart(request):
    customer = Customer.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items
    template = 'store/cart.html'
    form = HeightWidthForm()
    context = {
        'order': order,
        'items': items,
        'cart_items': cart_items,
        'form': form,
    }
    return render(request, template, context)


@login_required(login_url='store:login')
@checkout_clarence
def checkout(request):
    customer = Customer.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    template = 'store/checkout.html'
    cart_items = order.get_cart_items
    context = {
        'order': order,
        'items': items,
        'cart_items': cart_items,

=======
from django.shortcuts import render
from .models import Product, Order
from django.http import JsonResponse
import json

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
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
    }

    return render(request, template, context)


<<<<<<< HEAD
@login_required(login_url='store:login')
def payment_view(request):
    order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
    template = 'store/payment.html'
    context = {'order': order}

    return render(request, template, context)


@unacthenticated_user
def login_view(request):
    template = 'login.html'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:store')
        else:
            messages.error(request, 'Invalid username or password')
    context = {}

    return render(request, template, context)


@login_required(login_url='store:login')
def logout_view(request):
    logout(request)
    return redirect('store:store')


@unacthenticated_user
def register_view(request):
    template = 'register.html'
    form1 = CreateUserForm()
    form2 = CreateCustomerForm()
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CreateCustomerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            print( '\nboth forms valid\n')
            user = form1.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('store:login')       

    context = {
        'form1': form1,
        'form2': form2,
=======
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
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
    }

    return render(request, template, context)


<<<<<<< HEAD
@login_required(login_url='store:login')
=======
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
<<<<<<< HEAD
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderitem.quantity = orderitem.quantity + 1
        messages.success(request,product.name +' added to cart')
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity - 1
        messages.warning(request,product.name +' removed to cart')
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse('Item added into cart', safe=False)


@login_required(login_url='store:login')
def addHeightWigth(request, id):
    oi = OrderItem.objects.get(id=id)
    pre_height = oi.height
    pre_width =  oi.width
    if request.method == 'POST':
        form = HeightWidthForm(request.POST, instance=oi)
        if form.is_valid():
            if form.cleaned_data['height'] == None and form.cleaned_data['width'] == None:
                messages.info(request,'please enter heignt and width in feet before calculating')
            elif form.cleaned_data['width'] == None:
                f = form.save(commit=False)
                f.width = pre_width
                f.save()
            elif form.cleaned_data['height'] == None:
                f = form.save(commit=False)
                f.height = pre_height
                f.save()
            else:
                form.save()

    return redirect('store:cart')


@login_required(login_url='store:login')
def change_user_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.user.customer.name = name
        request.user.customer.save()
        return redirect('store:checkout')

    return redirect('store:store')


@login_required(login_url='store:login')
def change_user_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.username = email
        request.user.save()
        return redirect('store:checkout')

    return redirect('store:store')


@login_required(login_url='store:login')
def change_user_contact(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        request.user.customer.contact_no = contact
        request.user.customer.save()
        return redirect('store:checkout')

    return redirect('store:store')


@login_required(login_url='store:login')
def change_user_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        request.user.customer.address = address
        request.user.customer.save()
        return redirect('store:checkout')

    return redirect('store:store')


@login_required(login_url='store:login')
def processPayment(request):
    messages.success(request, 'your payment is processed successfully. order will be delivered within 3-5 working days')
    order = Order.objects.get(customer=request.user.customer, complete=False)
    order.complete = True
    order.save()

    return redirect('store:store')
=======

    customer = request.user.customer
    product = Product.objects.get( id=productId )

    order, created = Order.objects.get_or_create( customer=customer, complete=False )
    orderItem, created = orderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete() 

    return JsonResponse('Item was added successfully', safe=False)
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
