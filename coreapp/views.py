from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'coreapp/index.html')

def shop(request):
    return render(request, 'coreapp/shop.html')

def about(request):
    return render (request,'coreapp/about.html')

def contact(request):
    return render (request,'coreapp/contact.html')

def login(request):
    return render (request,'coreapp/login.html')