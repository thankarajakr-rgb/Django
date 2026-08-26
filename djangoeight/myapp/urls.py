from django.urls import path
from . import views


urlpatterns = [

    # HTML PAGES
    path('', views.home,name='home'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('table/',views.table,name='table'),
    path('student/', views.student_page,name='student'),
    path('student/update/<int:id>/', views.update,name='update'),
    path('student/delete/<int:id>/',views.delete,name='delete'),
    path('course/',views.course_page,name='course'),
    # ================================
    # COURSE API
    # ================================
    path('api/courses/', views.course_api,name='course_api'),
    path('api/courses/<int:id>/',views.course_detail_api,name='course_detail_api'),
    # ================================
    # STUDENT API
    # ================================
    path('api/students/',views.student_api,name='student_api'),
    path('api/students/<int:id>/',views.student_detail_api,name='student_detail_api'),
]