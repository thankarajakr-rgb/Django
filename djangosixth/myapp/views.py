from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from . models import Studentnew
from .serializers import Student_serializer
from rest_framework.decorators import api_view
from rest_framework import status


def home(request):
    return HttpResponse("<a href='/'>Home</a><a href='/index'>Index</a> <a href='/about'>About</a> <a href='/table'>About</a>  <a href='/student'>Student</a>I AM WORKING")

def index(request):
    if(request.method=="POST"):
      username=request.POST.get('username')
      password=request.POST.get('password')
      print(username,password)
      
      if (username=='Thankaraja' and password=="123"):
          print("Login Successful")
          return redirect('about')
      else:
          print("Invalid Creditionals")
          return render(request,'myapp/index.html',{
              "error":"Invalid Creditionals"
          })
          
      
      
    
    return render(request,'myapp/index.html')

def about(request):
    
   return render(request,'myapp/about.html')

def table(request):
    studentdetails=[
        {
        "id":101,
        "name":"Raja",
        "age":22
        },
        {
         "id":102,
         "name":"Gold",
        "age":14
                },
        {
          "id":103,
         "name":"Murugan",
         "age":10
                },
            ]
    
    return render(request,'myapp/table.html',{"students":studentdetails})


#def student(request):
  #  if(request.method=='POST'):
   #   course=request.POST['course']
    #    print(name,age,course)
        
     #   Studentnew.objects.create(
      #      name=name,
       #     age=age,
      #      course=course,
       # )
      #  student=Studentnew.objects.all()
      #  return render(request,'myapp/student.html',{"student":student})
   # student=Studentnew.objects.all()
#   return render(request,'myapp/student.html',{"student":student})


@api_view(['GET','POST','PUT','DELETE'])
def student(request):

    if request.method == "POST":
        serializer = Student_serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    student=Studentnew.objects.all()
    return render(request,'myapp/student.html',{"student":student})


def update(request,id):
    student=Studentnew.objects.get(id=id)
    if(request.method=='POST'):
        student.name=request.POST['name']
        student.age=request.POST['age']
        student.course=request.POST['course']
        student.save()
        return redirect('student')
        
    return render(request,'myapp/update.html',
                  {"student":student})


def delete(request,id):
     student=Studentnew.objects.get(id=id)
     student.delete()
     
     return redirect("student")
 
 

@api_view(['GET'])
def getdata(request):

     students = Studentnew.objects.all()
     serializer = Student_serializer(students, many=True)
     
     return Response(serializer.data)

   
    