
from unicodedata import category
from django.shortcuts import redirect, render
from django.views import View
from coreapp.models import *
from customer_purchase.models import *
from django.http import JsonResponse
import json

class CartView(View):
    
    def get(self,request): 
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer)
            items = order.orderitem_set.all()
        else:
            return redirect('login')  
        context ={"items":items,"order":order }
        return render(request, 'customer_purchase/cart.html',context) 

    
def updateItem(request,pk):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    
    if  Smart_phone.objects.filter(name=productId):
        product_phone =  Smart_phone.objects.get(name=productId)
        order, created = Order.objects.get_or_create(customer=customer)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product_phone=product_phone)
    
    elif Smart_watch.objects.filter(name=productId):
        product_watch =  Smart_watch.objects.get(name=productId)
        order, created = Order.objects.get_or_create(customer=customer)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product_watch=product_watch)
    
    elif Tabs.objects.filter(name=productId):
        product_tab =  Tabs.objects.get(name=productId)
        order, created = Order.objects.get_or_create(customer=customer)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product_tab=product_tab)  

    if action ==  'add':
        orderItem.quantity =  (orderItem.quantity +1)
            
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
            
    orderItem.save()
        
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added", safe=False)



