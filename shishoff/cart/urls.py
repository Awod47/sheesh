from django.urls import path
from .import views

urlpatterns= [
    path('cart/', views.the_cart, name= "cart_page"),
    path('checkout/', views.checkout, name= "checkout"),
    path('update_item/', views.updateItem, name= "update_item"),
    path('process_order/', views.processOrder, name= "process_order"),

]
#just the name of the page

