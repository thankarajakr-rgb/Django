from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
from rest_framework.response import Response
from . serializers import student_serializers
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

def home(request):
    return HttpResponse("<a href='/'>HOME</a> <a href='/about'>About</a> <a href='/index'>Index</a> <a href='/student'>Student</a>I AM THE BEST")
 
def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

# def student(request):
#     if(request.method=="POST"):
#         name=request.POST.get('name')
#         age=request.POST['age']
#         course=request.POST['course']
#         print(name,age,course)
        
#         Student.objects.create(
#             name=name,
#             age=age,
#             course=course
#         )
#         student=Student.objects.all()
#         return render(request,'myapp/student.html',{"student":student})
        
        
#     student=Student.objects.all()
#     return render(request,'myapp/student.html',{"student":student})



def updatestudent(request,id):
    student=Student.objects.get(id=id)
    
    if(request.method=="POST"):
        student.name=request.POST.get('name')
        student.age=request.POST.get('age')
        student.course=request.POST.get('course')
        
        student.save()
        
        return redirect('/student')
    return render(request,'myapp/updatestudent.html',{
        "student":student
    })
        
def deletestudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    
    return redirect('/student')
    
@api_view(['GET'])
def getdata(request):
    student=Student.objects.all()
    serializer=student_serializers(student,many=True)
    
    return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
def student(request):
    if request.method=="POST":
       serializer=student_serializers(data=request.data)
      
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
    
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    if request.method=='GET':
        student=Student.objects.all()
        return render(request,'myapp/student.html',{"student":student})
    
    
@api_view(['PUT','DELETE'])
def updateview(request,id):
   # if request.method=="PUT":
    try:
        student=Student.objects.get(id=id)
        
    
    except Student.DoesNotExist:
        return Response({
            "message":"Student Not Found"
        },status=status.HTTP_404_NOT_FOUND)
        
    if request.method=="PUT":    
        serializer= student_serializers(student,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        student.delete()
        
        return Response({
            "Message":"Student Deleted Successfully"
        },status=status.HTTP_200_OK)
        
        
        

    
        
        
                    
               
               
               
               
               
           
    
        
            

    
        
   
   
    








   
        


        
  
 

        
        
    
        

            
   
        
    
    

