from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="Home"),
    path('Signup',views.signup,name="Signup"),
    path('Login',views.login,name="Login"),
    path('Profile',views.profile,name="Profile"),
    path('PagesFaq',views.pages_faq,name="PagesFaq"),
    path('AddProduct',views.add_product,name="AddProduct"),
    path('UpdateProduct/<int:pk>',views.update_product,name="UpdateProduct"),
    path('DeleteProduct/<int:pk>',views.delete_product,name="DeleteProduct"),
    path('Testing',views.testing,name="Testing")
]
