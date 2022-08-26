from multiprocessing import context
from django.shortcuts import render
from .models import Smart_phone, Smart_watch, Tabs

def home(request):
    products = Smart_phone.objects.all()
    context = {"smartphones": products}
    return render(request,'coreapp/index.html')


def shop(request):
    phones = Smart_phone.objects.all()
    watches = Smart_watch.objects.all()
    tabs = Tabs.objects.all()
    context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
    return render(request, 'coreapp/productspage.html',context)


def shop_smartphones(request):
    phones =Smart_phone.objects.all()
    context ={"smartphones": phones}
    return render (request,'coreapp/productspage.html',context)

def about(request):
    return render (request,'coreapp/about.html')


def contact(request):
    return render (request,'coreapp/contact.html')


def login(request):
    return render (request,'coreapp/login.html')