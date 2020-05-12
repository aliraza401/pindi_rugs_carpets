from django.contrib import admin
<<<<<<< HEAD
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Shipping)
=======
from . import models

# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Product)
admin.site.register(models.Shipping)
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
