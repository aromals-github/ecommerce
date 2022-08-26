
from django.urls import path
from . import views


urlpatterns = [
    path ('' ,views.home , name = "home"),
    path ('contact/',views.contact , name = "contact"),
    path ('about/' ,views.about , name = "about"),
    path ('shop/' ,views.shop , name = "shop"),
    path ('login/' ,views.login,name ="login"),
    path ('shop/smartphones', views.shop_smartphones,name="shop_smartphones"),
]
