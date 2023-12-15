from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import *
from django.forms import ModelForm

#register
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))
        
    def save(self, commit=True):
        user = super(CreateUserForm,self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        if commit:
            user.save()
        return user
#login
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))

#edit
class EditUserForm(UserChangeForm):
    first_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
        }     
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            if i!= 'armature' or 'frame' or 'brush' or 'stator':
                self.fields[i].widget.attrs.update({'class':'form-control'})
            else:
                self.fields[i].widget.attrs.update({'class':'form-check-input'})
                
         
    