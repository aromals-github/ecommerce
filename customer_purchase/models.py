
from django.db import models
from coreapp.models import User,Smart_phone,Smart_watch,Tabs


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete= models.SET_NULL, null =True, blank =True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Smart_phone, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null= True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.address