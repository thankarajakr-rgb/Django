from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('new/',views.new),
    path('index/',views.index),
    path('home/',views.homepg,name='home'),
    path('about/',views.about,name='about'),
    
]