from django.forms import ModelForm
from coreapp.models import Smart_phone,Tabs,User,Smart_watch
from .models import Cart

class Cart_form(ModelForm):
    
    class Meta:
        model = Cart
        fields  = ['user','products']