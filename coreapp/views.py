from django.shortcuts import render,redirect, get_object_or_404, reverse
from .models import Smart_phone, Smart_watch, Tabs


def home(request):
    phones = Smart_phone.objects.all()
    watches = Smart_watch.objects.all()
    tabs = Tabs.objects.all()
    context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
    return render(request,'coreapp/index.html',context)


def shop(request):
    phones = Smart_phone.objects.all()
    watches = Smart_watch.objects.all()
    tabs = Tabs.objects.all()
    context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
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
    

def about(request):
    return render (request,'coreapp/about.html')


def contact(request):
    return render (request,'coreapp/contact.html')


def login(request):
    return render (request,'coreapp/login.html')