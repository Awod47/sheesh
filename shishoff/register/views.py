from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):

    #POST
    if response.method== 'POST':
        form= RegisterForm(response.POST)

        #check valid
        if form.is_valid():
            form.save()
            return redirect("/")
    
    else:
        form= RegisterForm()

    return render(response, "register/register.html", {"form": form})
