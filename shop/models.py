from django.db import models
import datetime as dt
import os
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def getFileName(request,filename):
    now = dt.datetime.now().strftime('%Y%m%d%H:%S')
    new_filename = "%s%s"%(now,filename)
    return os.path.join('uploads/',new_filename)
class Product(models.Model):
    id_number = models.CharField(max_length=150,null=False,blank=False)
    rpm = models.FloatField(null=False, blank=False)
    vibration = models.FloatField(null=False, blank=False)
    voltage = models.FloatField(null=False, blank=False)
    ampere = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    repaired_at = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    armature = models.BooleanField("is_armature",default=False)
    brush = models.BooleanField("is_brush",default=False)
    stator = models.BooleanField("is_stator",default=False)
    frame = models.BooleanField("is_frame",default=False)
    description = models.TextField(max_length=500,null=False,blank=True)
    
    def __str__(self):
        return self.id_number 
    
    @property
    def outputp(self):
        return self.rpm*21
    
    @property
    def inputp(self):
        return self.voltage*self.ampere