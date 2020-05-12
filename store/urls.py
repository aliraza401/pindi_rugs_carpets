<<<<<<< HEAD
from django.urls import path, include
from . import views
=======
from django.urls import path
from .import views
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8

app_name = 'store'

urlpatterns = [
<<<<<<< HEAD
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('payment/', views.payment_view, name='payment'),
    path('process_payment/', views.processPayment, name='process_payment'),
    path('view_product/<int:id>', views.view_product, name='view_product'),

    path('update/', views.updateItem, name='update_item'),
    path('addHeightWigth/<int:id>', views.addHeightWigth, name='addHeightWigth'),
    path('change_user_name/', views.change_user_name, name='change_user_name'),
    path('change_user_email/', views.change_user_email, name='change_user_email'),
    path('change_user_contact/', views.change_user_contact,
         name='change_user_contact'),
    path('change_user_address/', views.change_user_address,
         name='change_user_address'),
]
=======
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),

    path('updateItem/',views.updateItem,name='update_item'),
 
]

>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
