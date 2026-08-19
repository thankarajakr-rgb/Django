from django.urls import path
from . import views 

urlpatterns = [
    path('', views.raja),
    path('new/', views.new),
    path('home/', views.home,name="hom"),
    path('index/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('student/', views.addstudent),
    
]