from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
from rest_framework.response  import Response
from .serializers import student_serializer
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

def home(request):
    return HttpResponse(" <a href='/''>Home</a><a href='/index'>Index</a><a href='/about'>About</a> <a href='/student'>Student</a>i am Working")

def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

# def student(request):
#     if(request.method=="POST"):
#         name=request.POST['name']
#         age=request.POST['age']
#         course=request.POST['course']
#         print(name,age,course)
        
#         Student.objects.create(
#               name=name,
#               age=age,
#               course=course)
        
#         student=Student.objects.all()
#         return render(request,'myapp/student.html',{"student":student})
    
        
#     student=Student.objects.all()   
#     return render(request,'myapp/student.html',{"student":student})

@api_view(['GET','POST','PUT','DELETE'])
def student(request):
    if(request.method=="POST"):
        serializer=student_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
    student=Student.objects.all()   
    return render(request,'myapp/student.html',{"student":student})






def update(request,id):
    student=Student.objects.get(id=id)
    if(request.method=="POST"):
            student.name=request.POST['name']
            student.age=request.POST['age']
            student.course=request.POST['course']
            student.save()
            
            return redirect('student')
            
    
     
    
    return render(request,'myapp/update.html',{"student":student})



def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    
    return redirect('student')

@api_view(['GET'])
def getdata(request):
    student=Student.objects.all()
    serializer=student_serializer(student,many=True)
    return Response(serializer.data)


@api_view(['PUT','DELETE'])
def deleteview(request,id):
    try:
      student=Student.objects.get(id=id)
      
    except Student.DoesNotExist:
        return Response({
            "Message":"Student Does Not Exit"
        },status=status.HTTP_404_NOT_FOUND)  
        
    if request.method=="PUT":
        serializer=student_serializer(student,data=request.data)
        if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                
                
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    
    if request.method=="DELETE":
        student.delete()
        
        return Response({
            "Message":"Student Delted Successfully"
        },status=status.HTTP_200_OK)
        
        
            
    
    