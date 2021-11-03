from django.shortcuts import render, redirect
from .forms import NewsletterForm

# Create your views here.
def newsletter(request):
	if request.method == "POST":
		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect("/")
	
	else:
		form = NewsletterForm()

	return render(request, "base.html, ", {"form": form})