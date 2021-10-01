from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #use to create new user
from django.contrib.auth.models import User

#Check more about User Creation Form
class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]
