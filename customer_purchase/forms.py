from django.forms import ModelForm
from coreapp.models import Smart_phone,Tabs,User,Smart_watch


class Cart_form(ModelForm):
    
    class Meta:
        model = Smart_phone,Tabs,Smart_watch
        fields = '__all__'
        