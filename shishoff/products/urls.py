from django.urls import path
from .import views

urlpatterns= [
    path('products/', views.product_view, name= "product_page"),

]
#just the name of the page
