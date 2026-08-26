from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
from rest_framework.response import Response
from .serializers import Student_serializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    return HttpResponse("<a href='/'>HOME</a> <a href='/about'>About</a><a href='/student'>Student</a> <a href='/index'>Index</a> I am Working")
    
def index(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        
        if username=="Thankaraja" and password=='123':
            return redirect('about')
        
        else:
            return render(request,'myapp/index.html',{
                "error":"Invalid Creditionals"
            })
    
    
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

def student(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        course=request.POST['course']
        print(name,age,course)
        
        Student.objects.create(
            Name=name,
            Age=age,
            Course=course
        )
        
        students=Student.objects.all()
        return render(request,'myapp/student.html',{'students':students})
        
    students=Student.objects.all()   
    return render(request,'myapp/student.html',{'students':students})



def update(request,id):
    student=Student.objects.get(id=id)
    
    if request.method=="POST":
        student.Name=request.POST['name']
        student.Age=request.POST['age']
        student.Course=request.POST['course']
        student.save()
    
        return redirect('student')
    
    return render(request,'myapp/update.html',{'student':student})
    
    
def delete(request,id):
    students=Student.objects.get(id=id)    
    students.delete()
    
    return redirect('student')
    

def getdata(request):
    return HttpResponse("Super PA I am Working")   


@api_view(['GET'])
def studentapiget(request):
    student=Student.objects.all()
    serializer=Student_serializer(student,many=True)
    
    return Response(serializer.data)
   

@api_view(['POST'])
def studentapipost(request):
   if request.method=="POST":
       serializer=Student_serializer(data=request.data)
       
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       
       else:
           return Response(serializer.errors,status=status.HTTP_400_BADREQUEST)
       
        
        
@api_view(['PUT','DELETE'])
def studentapiput(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({
         "Message":"Student Not Found"
         },status=status.HTTP_404_NOT_FOUND)    
        
    if request.method=="PUT":
        serializer=Student_serializer(student,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)    
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        student.delete()
        return Response({
            "Message":"Student Deleted Successfully"
        },status=status.HTTP_200_OK)   
     

        
        
         
        
        
    
         
            
        
    
    
 

    
    
    