from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser

class Smart_phone(models.Model):
    phone_id = models.CharField(max_length=10,null=False,primary_key=True,default='')
    brand = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=50, null=False)
    colour = models.CharField( max_length=10, null= True)
    images = models.ImageField( upload_to="phone_image", blank=True)
    storage = models.IntegerField( default=128,validators=[MaxValueValidator(512),MinValueValidator(128)])
    price = models.DecimalField( max_digits=15, decimal_places=2,default=0.0)   
    instock =models.IntegerField( null=True)
    description =models.CharField( max_length=200,null=True)
    
    
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
    description = models.CharField( max_length=200,null=True)
    
    
    def __str__(self) :
        return self.name
    
  

class Tabs(models.Model):
    tab_id = models.CharField( max_length=20, null=False, primary_key=True)
    brand = models.CharField( max_length=20, null=False)
    name = models.CharField( max_length=30, null= False)
    colour = models.CharField( max_length=10, null= True)
    images = models.ImageField( upload_to="tablet_image", blank=True)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=15,decimal_places=2,default=0.0) 
    instock = models.IntegerField(null=True)
    storage = models.IntegerField(default=128,validators=[MinValueValidator(128),MaxValueValidator(1024)])
    description =models.CharField(max_length=200 ,null= True)
    
    
    def __str__(self) :
        return self.name
    
  
