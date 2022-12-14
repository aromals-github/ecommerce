from dataclasses import field
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
class UserLogIn(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email']