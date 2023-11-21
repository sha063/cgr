from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.contrib.auth.decorators import login_required

#links
Login = 'Login'
Profile = 'Profile'
PagesFaq = 'PagesFaq'
Home = 'Home'
Signup = 'Signup'
class profile_header:
    def __init__(self, icon, name,link):
        self.icon = icon
        self.name = name
        self.link = link

ProfileHeader = [profile_header('person','My Profile',Profile),
     #profile_header('gear','Account Settings','settings'),
     profile_header('question-circle','Need Help?',PagesFaq),
     profile_header('box-arrow-right','Sign Out',Login),]

#@login_required
def dashboard(request):
   template = loader.get_template('registration/dashboard.html')
   context = {
        'section':'dashboard',
        'title': 'CGR',
        'page_title': Home,
        'notifications': ['red', 'yellow', 'green'],
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'users':User.objects.all(),
        'profile_header':ProfileHeader,
    }
   return HttpResponse(template.render(context, request)) 

@login_required(login_url="Login")
def home(request):
    template = loader.get_template('shop/home.html')
    context = {

        'title': 'CGR',
        'page_title': Home,
        'notifications': ['red', 'yellow', 'green'],
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('shop/profile.html')
    context = {
        'page_title': Profile,
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template('shop/settings.html')
    context = {
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

def pages_faq(request):
    template = loader.get_template('shop/pages_faq.html')
    context = {
        'page_title':PagesFaq,
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    template = loader.get_template('shop/signup.html')
    context = {
        'page_title':PagesFaq,
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
        'registerform':form,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("Home")
    template = loader.get_template('shop/login.html')
    context = {
        'page_title':PagesFaq,
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
        'loginform':form,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    template = loader.get_template('shop/testing.html')
    context = {
        'category': Category.objects.all(),
        'product': Product.objects.all(),
        'profile_header':a,
    }
    return HttpResponse(template.render(context, request))


''' def testing(request):
    return render(request, 'shop/testing.html', {'category': Category.objects.all()}) '''
