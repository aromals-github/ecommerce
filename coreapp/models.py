from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser
from PIL import Image

class Smart_phone(models.Model):
    phone_id = models.CharField(max_length=10, null=False, primary_key=True, default='')
    brand = models.CharField(max_length=30, null=False)
    name = models.CharField(  max_length=50, null=False)
    colour = models.CharField( max_length=10, null= True)
    images = models.ImageField( upload_to="phone_image", blank=True)
    storage = models.IntegerField( default=128,validators=[MaxValueValidator(512),MinValueValidator(128)])
    price = models.DecimalField( max_digits=15, decimal_places=2,default=0.0)   
    instock =models.IntegerField( null=True)
    description =models.CharField( max_length=1000,null=True)
    operating_system = models.CharField(max_length=30,null=True)
    camera = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    
    
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural = "Smart Phones"
        
        
class Smart_watch(models.Model):
    watch_id = models.CharField(max_length=20,null=False,default='',primary_key=True)
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField( max_length=30, null= False)
    colour = models.CharField( max_length=10, null= True)
    images = models.ImageField( upload_to="watch_image", blank=True)
    size = models.IntegerField()
    price = models.DecimalField( max_digits=15, decimal_places=2, default=0)    
    instock_count = models.IntegerField( null=True)
    description = models.CharField( max_length=1000,null=True)
    
    def __str__(self) :
        return self.name
    

class Tabs(models.Model):
    tab_id = models.CharField( max_length=20, null=False, primary_key=True,default='')
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField( max_length=30, null= False)
    colour = models.CharField( max_length=10, null= True)
    images = models.FileField( upload_to="tablet_image")
    size = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=0.0,null=True) 
    instock = models.IntegerField(null=True)
    storage = models.IntegerField(default=128,validators=[MinValueValidator(128),MaxValueValidator(1024)])
    description =models.CharField(max_length=1000 ,null= True)
    
    def save(self, *args,**kwargs):
        if self.images:
            super().save(*args, **kwargs)
            img = Image.open(self.images.path)
            if img.height>700 or img.weight >700:
                output_size =(480,600)
                img.thumbnail(output_size)
                img.save(self.images.path)
    
    
    def __str__(self) :
        return self.name
    