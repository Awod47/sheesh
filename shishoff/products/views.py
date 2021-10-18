from django.shortcuts import render
from .models import *
# Create your views here.

def product_view(request):
    productss = Product.objects.all()
    return render(request, 'products/product_page.html', {'productss': productss})
#templates is the path so just add the other directory paths and go to urls
 
#product by ids; urls/id
#use filter instead of get as it gives a query set and not object
def product_detail(request,id):
    prod_desc= Product.objects.filter(id=id)
    return render(request, 'products/product_detail.html', {'prod_desc': prod_desc})