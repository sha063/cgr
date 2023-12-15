from django.contrib import admin
from .models import *
from . forms import *

class product_admin(admin.ModelAdmin):
  list_display = ('id_number','rpm','vibration','voltage','ampere','created_at','repaired_at','armature','brush','stator','frame','description')
  #list_display_links = ('category','name','description','image','quantity','original_price', 'selling_price')
  #list_filter = ('category','name','description','image','quantity','original_price','selling_price')
  #list_editable = ('name','description','image','quantity','original_price','selling_price')
  
admin.site.register(Product,product_admin)