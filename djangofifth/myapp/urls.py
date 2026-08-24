from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index/', views.index),
    path('about/', views.about),
    path('student/', views.student),
    path('student/update/<int:id>', views.updatestudent, name='updatestudent'),
    path('student/delete/<int:id>',views.deletestudent,name="deletestudent"),
    path('getdata/', views.getdata,name='student'),
    path('putdata/<int:id>',views.updateview,name='updateview'),
    
    
    
]