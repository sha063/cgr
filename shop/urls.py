from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,LoginView

urlpatterns = [
    path('',views.home,name="Home"),
    path('Signup',views.signup,name="Signup"),
    path('Login',views.login,name="Login"),
    path('Edit',views.edit,name="Edit"),
    path('Profile',views.profile,name="Profile"),
    path('PagesFaq',views.pages_faq,name="PagesFaq"),
    path('AddProduct',views.add_product,name="AddProduct"),
    path('UpdateProduct/<int:pk>',views.update_product,name="UpdateProduct"),
    path('DeleteProduct/<int:pk>',views.delete_product,name="DeleteProduct"),
    path('None/password/',PasswordResetView.as_view(),name="PasswordReset"),
    path('PasswordResetDone',PasswordResetDoneView.as_view(),name="PasswordResetDone"),
    path('PasswordResetConfirm',PasswordResetConfirmView.as_view(),name="PasswordResetConfirm"),
    path('PasswordResetComplete',PasswordResetCompleteView.as_view(),name="PasswordResetComplete"),
    path('Testing',views.testing,name="Testing")
]
