from django.contrib import admin
from .models import Smart_phone,Smart_watch,Tabs,User,Brands

admin.site.register(User)
admin.site.register(Smart_phone)
admin.site.register(Smart_watch)
admin.site.register(Tabs)
admin.site.register(Brands)