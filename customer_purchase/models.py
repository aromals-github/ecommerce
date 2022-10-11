from datetime import datetime
from django.db import models
from django.forms import CharField
from coreapp.models import User,Smart_phone,Smart_watch,Tabs


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    products = models.CharField(null=True,max_length = 90000)
    