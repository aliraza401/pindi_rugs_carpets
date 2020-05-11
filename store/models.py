from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username  # return email


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='product_img')
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property             # not give error while rendering image
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    data_ordred = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
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
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        price = self.height * self.width * self.product.price
        total_price = price * self.quantity
        return total_price


class Shipping(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.address
