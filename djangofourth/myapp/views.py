from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<a href='/'>Home</a><br> <a href='/index'>Index</a><br> <a href='/about'>About</a><br>  <br>Hi da its Working")
    

def index(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        print(request.POST)
        
        if (username=="Thankaraja" and password=="123"):
            print("LoginSuccessfull")
            return redirect('about')
        else:
            return render(request,'myapp/index.html',{
                "error":"Invalid Creditionals"
            })
        
    return render (request,'myapp/index.html')

def about(request):
    student_details=[{
        "id":101,
        "name":"Raja",
        "age":20,
        "course":"FSD"       
    },{
        "id":102,
        "name":"Gold",
        "age":12,
        "course":"SD"       
    },{
        "id":103,
        "name":"Raja",
        "age":17,
        "course":"SD"       
    },{
        "id":104,
        "name":"Raja",
        "age":25,
        "course":"D"       
    }]
    return render (request,'myapp/about.html',{
        "students":student_details
    })

