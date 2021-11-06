from django.urls import path
from .import views

urlpatterns= [
    path('cart/', views.the_cart, name= "cart_page"),
    path('checkout/', views.checkout, name= "checkout"),
]
#just the name of the page

