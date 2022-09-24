
from django.shortcuts import render,redirect, get_object_or_404, reverse
from .models import Brands, Smart_phone, Smart_watch, Tabs ,Brands
from django.db.models import Q
from django.views import View
from itertools import chain

def login(request):
    return render (request,'coreapp/login.html')

class HomeView(View):
    def get(self,request):
        phones = Smart_phone.objects.all()
        watches = Smart_watch.objects.all()
        tabs = Tabs.objects.all()
        context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
        return render(request,'coreapp/index.html',context)


def shop(request):
    # searchind enabled
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
    brand = Brands.objects.all()
    context = {'products':products , 'brands':brand}
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
        products = Smart_phone.objects.exclude(brand = 'google')
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
        products = Smart_watch.objects.exclude(brand = 'apple')
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
        products = Tabs.objects.exclude(brand = 'samsung')
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


def item(request,pk):
    
        if Tabs.objects.filter(name=pk):
            product_detail = Tabs.objects.filter(name=pk)
            all_tabs = Tabs.objects.all()
            context = {'products' : product_detail, 'all_items':all_tabs}
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_phone.objects.filter(name=pk):
            product_details = Smart_phone.objects.filter(name=pk)
            all_smartphones =Smart_phone.objects.all()
            context = {'products' : product_details , 'all_items':all_smartphones}
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_watch.objects.filter(name=pk):
            product_details = Smart_watch.objects.filter(name=pk)
            all_watch =Smart_watch.objects.all()
            context = {'products' : product_details, 'all_items':all_watch}
            return render (request, 'coreapp/item.html', context)
        
        
def add_product(request):
    return render(request,'home')


def cart(request):
    return render(request,'home')


def about(request):
    return render (request,'coreapp/about.html')


