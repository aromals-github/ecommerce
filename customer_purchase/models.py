
from email.policy import default
from tkinter import CASCADE

from django.db import models
from coreapp.models import *


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True,  blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null =True, blank =True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Smart_phone, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null= True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default = 1 ,null = True ,blank =True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.address