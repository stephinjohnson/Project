from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='custom_url_name'),
    path('home/',views.Home,name='homes'),
    path('reg/',views.Reg,name='Reg'),
    
    
]