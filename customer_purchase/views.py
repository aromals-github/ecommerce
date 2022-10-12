
from django.shortcuts import redirect, render
from django.views import View
from coreapp.models import Smart_phone,Tabs,Smart_watch,User
from customer_purchase.models import Cart



class CartView(View):
    
    def get(self,request,pk): 
        if request.user.is_authenticated:
            if Smart_phone.objects.filter(name=pk):
                product = Smart_phone.objects.filter(name=pk)
                item = product
                for item in item:
                    if item.instock > 0 :
                        user =  Cart.objects.filter(user=request.user)
                        print(user)
                        Cart.objects.create(
                                products = item
                            )
                    else:
                        Cart.objects.create(
                                user = request.user,
                                products = item
                            )
                    context ={'product':product}
                    return render(request,'customer_purchase/cart.html',context)
                        
                    
            elif Tabs.objects.filter(name=pk):
                product = Tabs.objects.filter(name=pk)
                item = product
                for item in item:
                    if item.instock > 0 :
                        user =  Cart.objects.filter(user=request.user)
                        print(user)
                        Cart.objects.create(
                                products = item
                            )
                    else:
                        Cart.objects.create(
                                user = request.user,
                                products = item
                            )
                    context ={'product':product}
                    return render(request,'customer_purchase/cart.html',context)
                            
            elif Smart_watch.objects.filter(name=pk):
                product = Smart_watch.objects.filter(name=pk)
                item = product
                for item in item:
                    if item.instock > 0 :
                        user =  Cart.objects.filter(user=request.user)
                        print(user)
                        Cart.objects.create(
                                products = item
                            )
                    else:
                        Cart.objects.create(
                                user = request.user,
                                products = item
                            )
                    context ={'product':product}
                    return render(request,'customer_purchase/cart.html',context)
 
        else:
            return redirect('login')
                    
                