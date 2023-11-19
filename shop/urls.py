from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Home',views.home,name="Home"),
    #path('login/',auth_views.LoginView.as_view(),name="login"),
    #path('Logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('Signup',views.signup,name="Signup"),
    path('Login',views.login,name="Login"),
    path('Profile',views.profile,name="Profile"),
    path('PagesFaq',views.pages_faq,name="PagesFaq"),
    path('Testing',views.testing,name="Testing")
]
