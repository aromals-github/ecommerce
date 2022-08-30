from email import message
from django.shortcuts import render,redirect
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
    context = {"tabs": tabs}
    return render (request, 'coreapp/productspage.html',context)


def item(request):
    phones = Smart_phone.objects.all()
    watches = Smart_watch.objects.all()
    tabs = Tabs.objects.all()
    context = {"smartphones": phones, "smartwatches":watches, "tabs":tabs}
    return render (request,'coreapp/item.html',context)


def about(request):
    return render (request,'coreapp/about.html')


def contact(request):
    return render (request,'coreapp/contact.html')


def login(request):
    return render (request,'coreapp/login.html')