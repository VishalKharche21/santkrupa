from django import forms
from django.forms import formset_factory
from .models import *
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-0 mt-4','placeholder':'*******'}))

class AddcustomerForm(forms.ModelForm):
    company_name=forms.CharField(max_length=100)
    address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    state=forms.CharField(max_length=100)
    gstno=forms.CharField(max_length=100)
    class Meta:
        model=customers
        fields="__all__"
