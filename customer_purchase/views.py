
from django.shortcuts import redirect, render
from django.views import View
from coreapp.views import login_register 
from coreapp.models import Smart_phone,Tabs,Smart_watch,User
from customer_purchase.models import Cart
from .forms import Cart_form


class CartView(View):
    
    def get(self,request,pk): 
        if request.user.is_authenticated:
            if Smart_phone.objects.filter(name=pk):
                product = Smart_phone.objects.filter(name=pk)
                item = product
                for item in item:
                    if item.instock > 0 :
                        user =  Cart.objects.filter(user=request.user)
                        if request.user == user: 
                            Cart.objects.create(
                                products = item
                            )
                        else:
                            Cart.objects.create(
                                user= request.user,
                                products = item
                            )
                        context ={'product':product}
                        return render(request,'customer_purchase/cart.html',context)
                        
                    
            elif Tabs.objects.filter(name=pk):
                product = Tabs.objects.filter(name=pk)
                items = product
                for item in items:
                    if item.instock>0 :   
                                context ={'product':product}
                                return render(request,'customer_purchase/cart.html',context)
                    else:
                        return render(request,'customer_purchase/home.html')
                            
            elif Smart_watch.objects.filter(name=pk):
                product = Smart_watch.objects.filter(name=pk)
                items = product
                for item in items:
                    if item.instock>0 :   
                        context ={'product':product}
                        return render(request,'customer_purchase/cart.html',context)
                    else:
                        return render(request,'customer_purchase/home')
 
        else:
            return redirect('login')
                    
                