from django.shortcuts import render,redirect
from django.contrib import messages
from coreapp.forms import UserCreation
from .models import  Smart_phone, Smart_watch, Tabs ,User
from django.db.models import Q
from django.views import View
from itertools import chain
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def login_register(request):
    
    if request.user.is_authenticated:
        return redirect('home')  
    form = UserCreation()           
    if  request.method =="POST":
        if request.POST.get('submit') == 'login':
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
        
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request,'User does not exits')
        
            user = authenticate(request,username = email,password =password)
      
            if user is not None:
                login (request,user)
                return redirect('home')
            else:
                messages.error(request,' user does not exits')
        
        elif request.POST.get('submit') == 'signup':
            form = UserCreation(request.POST)
            if form.is_valid():
                    user = form.save(commit= True)
                    user.username = user.username.lower()
                    user.save()
                    login(request,user)
                    return redirect('home')
            else:
                    messages.error(request,'An Error Occured During Registration')
                    return render(request, 'coreapp/login.html')
    return render(request, 'coreapp/login.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')
    

class HomeView(View):
    def get(self,request):
        
        phones = Smart_phone.objects.all()
        watches = Smart_watch.objects.all()
        tabs = Tabs.objects.all()
        context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
        return render(request,'coreapp/index.html',context)


def shop(request):
    # search enabled
    q = request.GET.get('q')
    if request.GET.get('q') != None:
        products = Smart_phone.objects.filter(
            Q(name__icontains = q) |
            Q(phone_id = q) | Q(brand__icontains =q)
        )or Smart_watch.objects.filter(
            Q(name__icontains = q) |
            Q(watch_id=q)
        )or Tabs.objects.filter(
            Q(name__icontains = q) |
            Q(tab_id = q)
        )
        context = {'products':products}
        return render(request,'coreapp/productspage.html',context)
    
    products = list(chain(Smart_phone.objects.all(),Tabs.objects.all(),Smart_watch.objects.all())) #combains two quries from two models to display at once....
    context = {'products':products }
    return render(request, 'coreapp/productspage.html',context)


def brand_smartphones(request,pk):
    id = pk 
    if id == 'apple' :
        products = Smart_phone.objects.filter(brand = 'apple') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'samsung':
        products = Smart_phone.objects.filter(brand = 'samsung')
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'google':
        products = Smart_phone.objects.filter(brand = 'google') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'others' : 
        products = Smart_phone.objects.filter(~Q(brand='apple'),~Q(brand='samsung'),~Q(brand='google'))
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)

def brand_watches(request,pk):
    id = pk 
    if id == 'apple' :
        products = Smart_watch.objects.filter(brand = 'apple') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'samsung':
        products = Smart_watch.objects.filter(brand = 'samsung') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'google':
        products = Smart_watch.objects.filter(brand = 'google') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'others' :
        products = Smart_watch.objects.filter(~Q(brand='apple'),~Q(brand='samsung'),~Q(brand ='google'))
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)

    
def brand_tabs(request,pk):
    id = pk 
    if id == 'apple' :
        products = Tabs.objects.filter(brand = 'apple') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'samsung':
        products = Tabs.objects.filter(brand = 'samsung') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'xiomi':
        products = Tabs.objects.filter(brand = 'xiomi') 
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)
    
    elif id == 'others' :
        products = Tabs.objects.filter(~Q(brand='apple'),~Q(brand='samsung'),~Q(brand='xiomi'))
        context = {'products':products}
        return render (request,'coreapp/productspage.html',context)


def shop_smartphones(request):
    phones = Smart_phone.objects.all()
    context = {"products": phones}
    return render (request,'coreapp/productspage.html',context)


def shop_smartwatches(request):
    watches = Smart_watch.objects.all()
    context = {"products": watches}
    return render (request,'coreapp/productspage.html',context)


def shop_tablets(request):
    tabs = Tabs.objects.all()
    context = { "products" :  tabs }
    return render (request, 'coreapp/productspage.html',context)


@login_required(login_url ='login')
def item(request,pk):
    
        if Tabs.objects.filter(name=pk):
            product_detail = Tabs.objects.filter(name=pk)
            all_tabs = Tabs.objects.filter(~Q(name=pk))
            context = {'products' : product_detail, 'all_items':all_tabs}
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_phone.objects.filter(name=pk):
            product_details = Smart_phone.objects.filter(name=pk)
            all_smartphones =Smart_phone.objects.filter(~Q(name=pk))
            specs = Smart_phone.objects.filter(name=pk).values('ram','camera')
            context = {'products' : product_details , 'all_items':all_smartphones, 'specs':specs}
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_watch.objects.filter(name=pk):
            product_details = Smart_watch.objects.filter(name=pk)
            all_watch = Smart_watch.objects.filter(~Q(name=pk))
            context = {'products' : product_details, 'all_items':all_watch}
            return render (request, 'coreapp/item.html', context)
        


@login_required(login_url ='login')
def cart(request,pk):
    return render(request,'coreapp/cart.html')


def about(request):
    return render (request,'coreapp/about.html')


