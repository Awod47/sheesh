from django.shortcuts import render
from .models import *
# Create your views here.

def product_view(request):
    productss = Product.objects.all()
    return render(request, 'products/product_page.html', {'productss': productss})
#templates is the path so just add the other directory paths and go to urls
 
