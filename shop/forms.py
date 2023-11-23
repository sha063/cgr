from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import *

#register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
#login
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','image','description','quantity','original_price','selling_price','trending']
        