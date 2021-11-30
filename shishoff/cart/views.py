from django.shortcuts import render
from django.http import JsonResponse
from .models import * 
import json
import datetime
# import Json

#CART.JS
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
		cartItems = order.get_cart_items
			
	else: 
		items= []
		#fix for logout
		order= {'get_cart_total': 0, 'get_cart_items': 0} #fix for unauthenticated cart_page.html user, returns empty
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context= {'items': items, 'order': order, 'cartItems':cartItems}
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
		cartItems = order.get_cart_items
	else: 
		items= []
		#fix for logout
		order= {'get_cart_total': 0, 'get_cart_items': 0} #fix for unauthenticated cart_page.html user, returns empty
		cartItems = order['get_cart_items']
		
	context= {'items': items, 'order': order}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	#logs items to backend
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('productId:', productId)

	#creates cutomer and order if not created

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	#if item already exists in cart, dont create new item
	#only change quantity
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	#if action is add, item is added to cart
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	#if number of a particular item i <0, take it off the cart
	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer = customer, complete = False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == float(order.get_cart_total):
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
				customer = customer,
				order = order,
				address = data['shipping']['address'],
				city = data['shipping']['city'],
				state = data['shipping']['state'],
				zipcode = data['shipping']['zipcode'],
			)

	else:
		print('User is logged in..')
	return JsonResponse('Payment complete', safe=False)