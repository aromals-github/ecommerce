from django.urls import path,include 
from. import views

urlpatterns = [
    
    path('',views.updateItem, name ="updatecart"),
    path('list/',views.CartView.as_view(), name ="cart"),
]
