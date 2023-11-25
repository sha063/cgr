from django.contrib import admin
from .models import *
from . forms import *

class category_admin(admin.ModelAdmin):
  list_display = ('name','description')

class product_admin(admin.ModelAdmin):
  list_display = ('category','id_number','description','rpm')
  #list_display_links = ('category','name','description','image','quantity','original_price', 'selling_price')
  #list_filter = ('category','name','description','image','quantity','original_price','selling_price')
  #list_editable = ('name','description','image','quantity','original_price','selling_price')
class user_admin(admin.ModelAdmin):
  list_display = ('username','email','password1','password2')
  
admin.site.register(Category,category_admin)
admin.site.register(Product,product_admin) 