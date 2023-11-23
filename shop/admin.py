from django.contrib import admin
from .models import *

class category_admin(admin.ModelAdmin):
  list_display = ('name','description')

class product_admin(admin.ModelAdmin):
  list_display = ('category','name','description','image','quantity','original_price','selling_price')
  #list_display_links = ('category','name','description','image','quantity','original_price', 'selling_price')
  #list_filter = ('category','name','description','image','quantity','original_price','selling_price')
  #list_editable = ('name','description','image','quantity','original_price','selling_price')

class profile_admin(admin.ModelAdmin):
  list_display = ('user','image')
  
admin.site.register(Category,category_admin)
admin.site.register(Product,product_admin) 
admin.site.register(Profile,profile_admin) 