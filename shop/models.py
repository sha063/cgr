from django.db import models
import datetime as dt
import os
from django.contrib.auth.models import User

def getFileName(request,filename):
    now = dt.datetime.now().strftime('%Y%m%d%H:%S')
    new_filename = "%s%s"%(now,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True, blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-default,1-hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    trending = models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name  
   
class Profile(models.Model):
    user =   models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to=getFileName)
    
    def __str__(self):
        return f'{self.user.username} Profile'