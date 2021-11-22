from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Customer(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank= True)
	name= models.CharField(max_length=150, null=True)
	email= models.EmailField(max_length=200, null=True)

	def __str__(self):
		return self.name 

class Order(models.Model):
	customer=models.ForeignKey(Customer, on_delete= models.SET_NULL, blank= True, null= True)
	dateordered= models.DateTimeField(auto_now_add= True)
	complete= models.BooleanField(default= False, null= True, blank= False)
	transaction_id= models.CharField(max_length= 200, null= True)

	def __str__(self):
		return str(self.id)

	@property
	#Total cart value, that's why for loop! :D (which is why created get_total first)
	def get_cart_total(self):
		orderitems= self.orderitem_set.all()
		total= sum([item.get_total for item in orderitems])
		return total

	#total quantity
	@property
	def get_cart_items(self):
		orderitems= self.orderitem_set.all()
		total= sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product= models.ForeignKey(Product, on_delete= models.SET_NULL, blank=True, null=True)
	#single order can have multiple order items
	order= models.ForeignKey(Order, on_delete= models.SET_NULL, blank=True, null=True)
	quantity= models.IntegerField(default=0, null=True, blank=True)
	date_added= models.DateTimeField(auto_now_add= True)

	#To render total
	@property
	def get_total(self):
		total= self.quantity* self.product.price #quantity already in the class, formula
		return total

class ShippingAddress(models.Model):
	#even if order gets deleted by reason x, would like to have the shipping address of the customer
	customer= models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True)
	order=models.ForeignKey(Order, on_delete= models.SET_NULL, blank=True, null=True)
	address= models.CharField(max_length= 200, null= True)
	city= models.CharField(max_length=200, null= True)
	state= models.CharField(max_length= 200, null= True)
	zipcode= models.CharField(max_length=200, null= True)
	date_added= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.address