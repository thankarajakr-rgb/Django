from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Students


def raja(request):
    return HttpResponse("<a href='/'>Raja</a><br> <a href='/new'>New</a><br> <a href='/home'>Home</a><br> <a href='/about'>About</a><br> <a href='/index'>Index</a> <br>Hi da its Working")

def new(request):
    return HttpResponse("This is Raja Thankarjak")

def home(request):
    return render(request,'myapp/home.html')

def index(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        print(request.POST)
        
        if (username=="Thankaraja" and password=="123"):
            print("Login Successful")
            #return redirect("hom")
            return render(request,'myapp/index.html',{
                            "erro":"Login Successful"
                        })
        else:
            return render(request,'myapp/index.html',{
                "erro":"Invalide creditionls"
            })
        
        
    return render(request,'myapp/index.html')

def about(request):
    student_details=[{
                      "id":101,
                      "name":"suresh",
                      "age":20,
                      "course":"FSD"
                    
                      },{
                      "id":102,
                      "name":"raja",
                      "age":17,
                      "course":"SD"
                    
                      },{
                      "id":103,
                      "name":"gold",
                      "age":16,
                      "course":"ST"
                    
                      },
                      {
                      "id":104,
                      "name":"goldraja",
                      "age":30,
                      "course":"ST"
                    
                      }
                     ]
    return render(request,'myapp/about.html',{"students":student_details})


def addstudent(request):
    if(request.method=="POST"):
        name=request.POST['name']
        age=request.POST['age']
        course=request.POST['course']
        print(name,age,course)
    
        Students.objects.create(
               name=name,
                age=age,
               course=course
         )
        students=Students.objects.all()
        return render(request,'myapp/studentoperation.html',{"students":students})
    students=Students.objects.all()
  
    
    return render(request,'myapp/studentoperation.html',{"students":students})
