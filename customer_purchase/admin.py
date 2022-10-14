from django.contrib import admin
from .models import Order,OrderItem,ShippingAddress
# Register your models here.

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("customer","date_ordered")
    
@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ("product","order")
    
    
@admin.register(ShippingAddress)
class ShippingAddress(admin.ModelAdmin):
    list_display = ("customer","address")