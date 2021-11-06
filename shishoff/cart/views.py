from django.shortcuts import render

# Create your views here.
def the_cart(request):
	context= {}
	return render(request, 'store/cart_page.html', context)

def checkout(request):
	context= {}
	return render(request, 'store/checkout.html', context)