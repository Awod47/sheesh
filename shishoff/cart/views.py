from django.shortcuts import render
from .models import * 


# Create your views here.
def the_cart(request):
	if request.user.is_authenticated:
		#One to one relationship
		customer= request.user.customer
		#if not ordered, create one
		#Read docs
		order, created= Order.objects.get_or_create(customer= customer, complete= False)
		#use the object 'order' not class 'order'
		items= order.orderitem_set.all()
	else: 
		items= []
		#fix for logout
		order= {'get_cart_total': 0, 'get_cart_items': 0 } #fix for unauthenticated cart_page.html user, returns empty

	context= {'items': items, 'order': order}
	return render(request, 'store/cart_page.html', context)

def checkout(request):
	
	if request.user.is_authenticated:
		#One to one relationship
		customer= request.user.customer
		#if not ordered, create one
		#Read docs
		order, created= Order.objects.get_or_create(customer= customer, complete= False)
		#use the object 'order' not class 'order'
		items= order.orderitem_set.all()
	else: 
		items= []
		#fix for logout
		order= {'get_cart_total': 0, 'get_cart_items': 0 } #fix for unauthenticated cart_page.html user, returns empty

	context= {'items': items, 'order': order}
	return render(request, 'store/checkout.html', context)