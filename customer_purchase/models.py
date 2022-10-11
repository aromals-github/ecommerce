
from django.db import models
from coreapp.models import User,Smart_phone,Smart_watch,Tabs


# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    product_smartphones = models.ForeignKey(Smart_phone,on_delete = models.CASCADE,null=True) 
    product_watches = models.ForeignKey(Smart_watch,on_delete = models.CASCADE,null=True)
    product_tabs = models.ForeignKey(Tabs,on_delete = models.CASCADE,null=True)
    all_products ={
        'products1':product_smartphones,
        'products2':product_watches,
        'products3':product_tabs
    }