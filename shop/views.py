from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test

#
p = Product.objects.all()

#links
Login = 'Login'
Profile = 'Profile'
About = 'About'
PagesFaq = 'PagesFaq'
Home = 'Home'
Signup = 'Signup'

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

class c:
    def __init__(self, icon,field,subject1,subject2):
        self.icon = icon
        self.field = field
        self.subject1 = subject1
        self.subject2 = subject2

class part:
    def __init__(self,name,image,description):
        self.name = name
        self.image = image
        self.description = description

def email_check(user):
    return user.email.endswith('@example.com')

ProfileHeader = [profile_header('person','My Profile',Profile),
     profile_header('question-circle','Need Help?',PagesFaq),
     profile_header('box-arrow-right','Sign Out',Login),]

alist = [
    a('Home','house',[b('Table','#table'),]),
    a('Dashboard','menu-button-wide',[b('Home','Home'), b('About','About'),b('Pages FAQ','PagesFaq'),]),
    a('Database','database',[b('Add Product','admin')]),
    a('Users','person-circle',[b('Profile','Profile'),b('Edit Profile','Edit'),]),
]

parts = [
    part('Armature','assets/img/p1.jpg',"The spinning heart, this iron core with wire coils generates its own magnetic field when juiced with electricity. Think of it as the athlete, converting energy into movement."),
    part('Brushes','assets/img/p3.jpg',"The electrical conductors, these carbon contacts dance across a segmented ring (commutator) to keep the current flowing in the right direction. Picture them as the coach, guiding the athlete's every step."),
    part('Stator','assets/img/p2.jpg',"The muscle of the motor, this stationary ring houses magnets that create a constant magnetic field. Imagine it as the gym's power grid, energizing the workout."),
    part('Commutator','assets/img/p4.jpg',"The conductor's baton, this segmented ring switches the current in the armature coils at just the right moment, ensuring smooth, continuous rotation. Imagine it as the conductor's cue, keeping the orchestra in perfect harmony."),
    ]

def home(request):
    pre = 'assets/img/slides-'
    suf = '.jpg'
    l = ['active','','']
    m = ['aria-current="true"','','']
    z = [] 
    def stringify():
        for i,j,k in zip(range(1,4),l,m):
            list = {}
            list['loc'] = pre+str(i)+suf
            list['stat'] = j
            list['n'] = str(i)
            list['nu'] = str(i-1)
            list['ac'] = k
            z.append(list)
        return z
    template = loader.get_template('shop/home.html')
    context = {
        'title': 'CGR',
        'page_title': Home,
        'notifications': ['red', 'yellow', 'green'],
        'product': Product.objects.all(),
        'profile_header':ProfileHeader,
        'alist':alist,
        'dict':stringify(),
        'list':['prev','next'],
        'parts': parts,
        
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="Login")
def profile(request):
    template = loader.get_template('shop/profile.html')
    context = {
        'page_title': Profile,
        'profile_header':ProfileHeader,
        'alist':alist[1:4],
    }
    return HttpResponse(template.render(context, request))

def about(request):
    d = [
        c('geo-alt','Address','Sri Lanka German Railway Technical Training Centre,','Off, B545, 10370'),
        c('telephone','Call Us','+94 112 605 625','+94 112 632 391'),
        c('envelope','Email Us','cgtti@sltnet.lk','https://www.cgtti.lk'),
         ]
    template = loader.get_template('shop/about.html')
    context = {
        'page_title': About,
        'profile_header':ProfileHeader,
        'alist':alist[1:4],
        'list':d,
    }
    return HttpResponse(template.render(context, request))

def pages_faq(request):
    template = loader.get_template('shop/pages_faq.html')
    context = {
        'page_title':PagesFaq,
        'profile_header':ProfileHeader,
        'alist':alist[1:4],
    }
    return HttpResponse(template.render(context, request))

''' @login_required(login_url="Login")
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
    return redirect("Home") '''

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
