"""
URL configuration for ims project.
"""
from django.urls import path
from  . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('manage-store',views.manage_store,name='store'),
    path('inventory',views.get_inventory,name='inventory'),
    path('invoice',views.get_invoice,name='invoice'),
    path('search',views.search_bikes,name='search')    
]

