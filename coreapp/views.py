from django.shortcuts import render,redirect, get_object_or_404, reverse
from .models import Smart_phone, Smart_watch, Tabs
from django.db.models import Q

def login(request):
    return render (request,'coreapp/login.html')


def home(request):
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
            Q(name__icontains=q) |
            Q(phone_id = q) | Q(name__icontains =q) 
        )or Smart_watch.objects.filter(
            Q(name__icontains=q) |
            Q(watch_id=q)
        )or Tabs.objects.filter(
            Q(name__icontains =q) |
            Q(tab_id = q)
        )
        context = {'products':products}
        return render(request,'coreapp/productspage.html',context)

    phones = Smart_phone.objects.all()
    watches = Smart_watch.objects.all()
    tabs = Tabs.objects.all()
    context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs }
    return render(request, 'coreapp/productspage.html',context)


def shop_smartphones(request):
    phones = Smart_phone.objects.all()
    context = {"smartphones": phones}
    return render (request,'coreapp/productspage.html',context)


def shop_smartwatches(request):
    watches = Smart_watch.objects.all()
    context = {"smartwatches": watches}
    return render (request,'coreapp/productspage.html',context)


def shop_tablets(request):
    tabs = Tabs.objects.all()
    context = { "tabs" :  tabs }
    return render (request, 'coreapp/productspage.html',context)


def item(request,pk):
    
        if Tabs.objects.filter(name=pk):
            product_detail = Tabs.objects.filter(name=pk)
            all_tabs = Tabs.objects.all()
            context = { 'products' : product_detail, 'all_items':all_tabs }
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_phone.objects.filter(name=pk):
            product_details = Smart_phone.objects.filter(name=pk)
            all_smartphones =Smart_phone.objects.all()
            context = { 'products' : product_details , 'all_items':all_smartphones}
            return render (request, 'coreapp/item.html', context)
        
        elif Smart_watch.objects.filter(name=pk):
            product_details = Smart_watch.objects.filter(name=pk)
            all_watch =Smart_watch.objects.all()
            context = { 'products' : product_details, 'all_items':all_watch}
            return render (request, 'coreapp/item.html', context)
        

def add_product(request):
    return render(request,'home')


def cart(request):
    return render(request,'home')


def about(request):
    return render (request,'coreapp/about.html')


