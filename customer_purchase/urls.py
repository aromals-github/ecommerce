from django.urls import path,include 
from. import views

urlpatterns = [
    
    path('',views.CartView.as_view(), name ="cart"),
    path('updateitem/',views.updateItem, name ="itemcart")
]
