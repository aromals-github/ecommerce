from django.urls import path
from . import views

urlpatterns =[
    path ('' ,views.HomeView.as_view(), name = "home"),
    path ('login/', views.login, name = "login"),
    path ('about/',views.about, name = "about"),
    path ('shop/', views.shop, name = "shop"),
    path ('shop/smartphones/', views.shop_smartphones, name = "shop_smartphones"),
    path ('shop/smartwatches/', views.shop_smartwatches, name = "shop_smartwatches"),
    path ('shop/tablets/', views.shop_tablets, name = "shop_tablets"),
    path ('shop/item/<str:pk>/', views.item, name = "item"),
    path ('shop/smartphones/samsung',views.brand_smartphones,name = "branded_smartphones"),
]
