
from django.shortcuts import redirect, render
from django.views import View
from coreapp.models import Smart_phone,Tabs,Smart_watch,User
from customer_purchase.models import Order,OrderItem,ShippingAddress



class CartView(View):
    
    def get(self,request,pk): 
        if request.user.is_authenticated:
            customer =request.user.customer
            order, created = Order.objects.get_or_created(customer=customer)
            items = order.orderitem_set.all()
        else:
            return redirect('login')  
        context ={items}
        return render(request, 'customer_purchase',context) 
