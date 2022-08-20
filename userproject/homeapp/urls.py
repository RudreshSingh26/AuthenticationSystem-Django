from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.index, name='index' ),
    path('userlogin', views.userlogin, name='userlogin' ),
    path('userlogout', views.userlogout, name='userlogout' )
    
]
