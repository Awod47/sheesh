from django.urls import path
from .import views

urlpatterns= [
    path('products/', views.product_view, name= "product_page"),
    path('products/<int:id>/', views.product_detail, name= "product_detail"),
]
#just the name of the page

