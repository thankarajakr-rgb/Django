from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('about/',views.about),
    path('student/',views.student,name="student"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('getdata/',views.getdata,name="getdata"),
    path('deleteview/<int:id>',views.deleteview,name='deleteview'),


]
