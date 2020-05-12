from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username  # return email
=======
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.email
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
<<<<<<< HEAD
    image = models.ImageField(null=True, blank=True, upload_to='product_img')
    price = models.FloatField()
=======
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='product_img')
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8

    def __str__(self):
        return self.name

<<<<<<< HEAD
    @property             # not give error while rendering image
=======
    # not give error while rendering image
    @property
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
<<<<<<< HEAD
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    data_ordred = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=350, null=True, blank=True)
=======
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordred = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=350, null=True)
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
<<<<<<< HEAD
        order_items = self.orderitem_set.all()
        total = sum([i.get_total for i in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([i.quantity for i in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    height = models.FloatField(default=1, null=True, blank=True)
    width = models.FloatField(default=1, null=True, blank=True)
=======
        orderitems = self.orderitem_set.all()
        total = sum( [ item.get_total  for item in orderitems ] )
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum( [ item.quantity  for item in orderitems ] )
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, default=False)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, default=False)
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
<<<<<<< HEAD
        price = self.height * self.width * self.product.price
        total_price = price * self.quantity
        return total_price
=======
        total = self.quantity * self.product.price
        return total
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8


class Shipping(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
<<<<<<< HEAD
    date_added = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
=======
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8

    def __str__(self):
        return self.address
