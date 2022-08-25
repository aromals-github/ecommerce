from re import M
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Smart_phone(models.Model):
    brand = models.CharField( max_length=30, null=False)
    phone_name = models.CharField( max_length=50, null=False, primary_key=True)
    phone_colour = models.CharField( max_length=10, null= True)
    phone_images = models.ImageField( upload_to="phone_image",blank=True)
    storage = models.IntegerField(default=128,validators=[MaxValueValidator(512),MinValueValidator(128)])
    
    instock_count =models.IntegerField(null=True)
    
    def __str__(self) :
        return self.phone_name
    
    class Meta:
        verbose_name_plural = "Smart Phones"

class Smart_watch(models.Model):
    brand = models.CharField( max_length=20, null=False, default="")
    watch_name = models.CharField( max_length=30,null= False, primary_key=True,default="")
    watch_colour = models.CharField( max_length=10, null= True)
    watch_images = models.ImageField( upload_to="watch_image", blank=True)
    size = models.IntegerField()
    
    instock_count = models.IntegerField(null=True)
    
    def __str__(self) :
        return self.watch_name
    
  

class Tabs(models.Model):
    brand = models.CharField( max_length=20, null=False)
    tab_name = models.CharField( max_length=30,null= False, primary_key=True)
    tablet_colour = models.CharField( max_length=10, null= True)
    tablet_images = models.ImageField( upload_to="tablet_image", blank=True)
    size = models.IntegerField()
   
    instock_count = models.IntegerField(null=True)
    storage = models.IntegerField(default=128,validators=[MaxValueValidator(128),MinValueValidator(1024)])
    
    
    def __str__(self) :
        return self.tab_name
    
  
    
    