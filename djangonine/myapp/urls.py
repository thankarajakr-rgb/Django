from . import views 
from django.urls import path,include

urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('student/',views.student,name='student'),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("getdata/", views.getdata, name="getdata"),
    path("studentapiget/", views.studentapiget, name="studentapiget"),
    path("studentapipost/", views.studentapipost, name="studentapipost"),
    path("studentapiput/<int:id>", views.studentapiput, name="studentapiput"),
    
   
   
]
