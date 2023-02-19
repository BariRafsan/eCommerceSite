from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']

class CustomerProfileForm(forms.ModelForm):
	class Meta:
            model = Customer
            fields = ['name','email','phone','password']
            widgets = {
		    'name': forms.TextInput(attrs={'class': 'form-control'}),
		    'email': forms.TextInput(attrs={'class': 'form-control'}),
		    'phone': forms.TextInput(attrs={'class': 'form-control'}),
		    'password': forms.TextInput(attrs={'class': 'form-control'}),
	    }