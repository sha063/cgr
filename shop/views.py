from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.contrib.auth.decorators import login_required

#
p = Product.objects.all()

#links
Login = 'Login'
Profile = 'Profile'
PagesFaq = 'PagesFaq'
Home = 'Home'
Signup = 'Signup'

#strings


class profile_header:
    def __init__(self, icon, name,link):
        self.icon = icon
        self.name = name
        self.link = link

class a:
    def __init__(self, name,icon,list):
        self.name = name

        self.list = list
        self.icon = icon

class b:
    def __init__(self, name, link):
        self.name = name
        self.link = link

ProfileHeader = [profile_header('person','My Profile',Profile),
     #profile_header('gear','Account Settings','settings'),
     profile_header('question-circle','Need Help?',PagesFaq),
     profile_header('box-arrow-right','Sign Out',Login),]

alist = [
    a('Dashboard','menu-button-wide',[b('Home',''), b('About','About'),b('Pages FAQ','PagesFaq'),]),
    a('Database','database',[b('Add Product','AddProduct')]),
    a('Users','person-circle',[b('Profile','Profile'),b('Edit Profile','Edit'),]),
    a('Home','house',[b('Table','#table'),]),
]

@login_required(login_url="Login")
def home(request):
    template = loader.get_template('shop/home.html')
    context = {
        'title': 'CGR',
        'page_title': Home,
        'notifications': ['red', 'yellow', 'green'],
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'product_fields': Product,
        'profile_header':ProfileHeader,
        'alist':alist,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def profile(request):
    template = loader.get_template('shop/profile.html')
    context = {
        'page_title': Profile,
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def pages_faq(request):
    template = loader.get_template('shop/pages_faq.html')
    context = {
        'page_title':PagesFaq,
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def add_product(request):
    form = AddProductForm()
    if request.method == "POST":
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Home")
        else:
            form = AddProductForm()
    template = loader.get_template('shop/add_product.html')
    context = {
        'addform':form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = AddProductForm(instance=product)
    if request.method == "POST":
        form = AddProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect("Home")
        else:
            form = AddProductForm()
    template = loader.get_template('shop/update_product.html')
    context = {
        'updateform':form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("Home")

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    template = loader.get_template('shop/signup.html')
    context = {
        'signupform':form,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("Profile")
    template = loader.get_template('shop/login.html')
    context = {
        'loginform':form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def edit(request):
    form = EditUserForm()
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("Profile")
    else:
        form = EditUserForm()
    template = loader.get_template('shop/edit.html')
    context = {
        'editform':form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def testing(request):
    template = loader.get_template('shop/testing.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


''' def testing(request):
    return render(request, 'shop/testing.html', {'category': Category.objects.all()}) '''
