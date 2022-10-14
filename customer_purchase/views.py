
from django.shortcuts import redirect, render
from django.views import View
from coreapp.models import *
from customer_purchase.models import *
from django.http import JsonResponse
import json

class CartView(View):
    
    def get(self,request,pk): 
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer)
            items = order.orderitem_set.all()
        else:
            return redirect('login')  
        context ={"items":items,"order":order }
        return render(request, 'customer_purchase/cart.html',context) 

    
def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

    return JsonResponse("Item was added", safe=False)