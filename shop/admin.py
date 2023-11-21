from django.contrib import admin
from .models import *

class category_admin(admin.ModelAdmin):
  list_display = ('name','description')

class product_admin(admin.ModelAdmin):
  list_display = ('category','name','description','image','quantity','original_price','selling_price')
class users_admin(admin.ModelAdmin):
  list_display = ('name','image','password')
  
admin.site.register(Category,category_admin)
admin.site.register(Product,product_admin) 