
from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    username = models.CharField(max_length= 200,null =True,unique=True)
    email = models.EmailField(unique=True,null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email' ]
    
    def __email__(self):
        return self.email
    
    
class Smart_phone(models.Model):
    phone_id = models.CharField(max_length=10, null=False, primary_key=True, default='')
    brand = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=50, null=False)
    colour = models.CharField(max_length=10, null= True)
    images = models.ImageField(upload_to="phone_image", blank=True)
    storage = models.IntegerField(default=128, validators=[MaxValueValidator(512), MinValueValidator(128)])
    price = models.IntegerField(default=0)   
    instock =models.IntegerField(null=True)
    description =models.CharField(max_length=1000, null=True)
    operating_system = models.CharField(max_length=30, null=True)
    camera = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(default = datetime.now())# has to change to---auto_now_add = True
    ram = models.IntegerField(default=4,null=True,blank=True)
    
    def __str__(self) :         
        return self.name
    
    def save(self, *args,**kwargs):
        if self.images:
            super().save(*args, **kwargs)
            img = Image.open(self.images.path)
            if img.height>700 :
                output_size =(480,600)
                img.thumbnail(output_size)
                img.save(self.images.path)

    class Meta:
        verbose_name_plural = "Smart Phones"


class Smart_watch(models.Model):
    watch_id = models.CharField(max_length=20,null=False,default='',primary_key=True)
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField( max_length=30, null= False)
    colour = models.CharField( max_length=10, null= True)
    images = models.ImageField( upload_to="watch_image", blank=True)
    size = models.IntegerField()
    price = models.IntegerField(default=0)    
    instock = models.IntegerField( null=True)
    description = models.CharField( max_length=1000,null=True)
    date_added = models.DateTimeField(default = datetime.now())# has to change to---auto_now_add = True

    def save(self, *args,**kwargs):
        if self.images:
            super().save(*args, **kwargs)
            img = Image.open(self.images.path)
            if img.height>700 :
                output_size =(480,600)
                img.thumbnail(output_size)
                img.save(self.images.path)
                
    def __str__(self) :
        return self.name
        
class Tabs(models.Model):
    tab_id = models.CharField( max_length=20, null=False, primary_key=True,default='')
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField( max_length=30, null= False)
    colour = models.CharField( max_length=10, null= True)
    images = models.FileField( upload_to="tablet_image")
    display_size = models.IntegerField(null=True)
    price = models.IntegerField(default=0) 
    instock = models.IntegerField(null=True)
    storage = models.IntegerField(default=128,validators=[MinValueValidator(128),MaxValueValidator(1024)])
    description =models.CharField(max_length=1000 ,null= True)
    ram = models.IntegerField(default=4,null=True,blank=True)
    date_added = models.DateTimeField(default = datetime.now())# has to change to---auto_now_add = True
    
    def save(self, *args,**kwargs):
        if self.images:
            super().save(*args, **kwargs)
            img = Image.open(self.images.path)
            if img.height>700 :
                output_size =(480,600)
                img.thumbnail(output_size)
                img.save(self.images.path)
    
    def __str__(self) :
        return self.name
    


