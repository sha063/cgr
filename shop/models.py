from django.db import models
import datetime as dt
import os
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def getFileName(request,filename):
    now = dt.datetime.now().strftime('%Y%m%d%H:%S')
    new_filename = "%s%s"%(now,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    #image = models.ImageField(upload_to=getFileName,null=True, blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    id_number = models.CharField(max_length=150,null=False,blank=False)
    #image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    #quantity = models.IntegerField(null=False,blank=False)
    rpm = models.CharField(null=False,blank=False,max_length=15)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name  