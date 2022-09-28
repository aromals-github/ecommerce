from django.contrib import admin
from .models import Smart_phone,Smart_watch,Tabs,User,SmartphoneInfo

admin.site.register(User)


@admin.register(SmartphoneInfo)
class SmartphoneInfo(admin.ModelAdmin):
    list_display =('info','ram')
    

@admin.register(Smart_phone)
class Smartphones(admin.ModelAdmin):
    list_display = ('brand','name','colour','storage')
    
    
@admin.register(Smart_watch)
class Smartwatch(admin.ModelAdmin):
    list_display = ('brand','name','colour','size')
   
    
@admin.register(Tabs)
class Tablets(admin.ModelAdmin):
    list_display = ('brand','name','colour','storage')