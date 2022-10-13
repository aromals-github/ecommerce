from django.db import models
from coreapp.models import User,Smart_phone,Smart_watch,Tabs


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    total_cost = models.IntegerField(null=True,blank=True)

    def __char__(self):
        return self.user

class CartProducts(models.Model):
    user = models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True)
    products_name = models.ForeignKey(Smart_phone,on_delete = models.CASCADE,related_name='cartproducts',null=True)
    products = models.CharField(null=True,max_length = 90000)
    
    def __char__(self):
        return self.user