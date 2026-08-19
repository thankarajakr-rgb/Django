from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse("helloo django")


def new(request):
    return HttpResponse("This is new")

def index(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        print(request.POST)
        
        if(username=="Thankaraja" and password=="123"):
            print("Login Successful")
            return redirect("home")
        else:
          return render(request,'myapp/index.html',{
               "error":"Invalid Credientials"
           })
          
       
    return render(request,'myapp/index.html')       
    

def homepg(request):
    return render(request,'myapp/homepg.html')

def about(request):
    return render(request,'myapp/about.html')