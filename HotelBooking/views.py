from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from superuser.models import Manager
from django.contrib.auth import login, logout, authenticate

def home(request):
    if request.method=="POST":
        fn=request.POST["first_name"]
        ln=request.POST["last_name"]
        un=request.POST["username"]
        email=request.POST["email"]
        pwd=request.POST["password"]
        image=request.FILES["profile_image"]
        age=request.POST["age"]
        add=request.POST["address"]
        mobile=request.POST["mobile"]
        gen=request.POST["gender"]
        print('hello')
        obj=User(first_name=fn,last_name=ln,username=un,email=email,password=make_password(pwd))
        obj.save()
        uobj=UserProfile(user=obj,proimg=image,age=age,address=add,mobile=mobile,gender=gen,usertype='user')
        uobj.save()
        return redirect("/login/")
    return render(request,"home.html")


def login_call(request):
    if request.method=="POST":
        print('hello')
        un=request.POST["username"]
        pwd=request.POST["password"]
        log=authenticate(username=un,password=pwd)
        if log:
            login(request,log)
            pro=UserProfile.objects.get(user__username=request.user)
            
            if pro.usertype == "superuser":
                return redirect('/superuser/home/')   
            elif pro.usertype == "manager":
                return redirect('/manager/home/')
            elif pro.usertype == "user":
                return redirect('/user/home/')
        else:
            return HttpResponse("<h1>invalid user and password</h1>")
            
    return render(request,"login.html")

def signup(request):
    
    return render(request,"home.html")

def logout_call(request):
	logout(request)
	return redirect('/home/')

def profile(request):
    obj=UserProfile.objects.get(user__username=request.user)
    
    if request.method=='POST':
        name=request.POST["fname"]
        lname = request.POST["lname"]
        uname = request.POST["username"]
        
        email =request.POST["email"]
        add =request.POST["address"]
        mob = request.POST["mobile"]
        uobj1 =User.objects.filter(username=request.user)
        obj=UserProfile.objects.filter(user__username=request.user)
   
        uobj1.update(first_name=name,last_name=lname,username=uname,email=email)
        obj.update(address=add,mobile=mob)
        return redirect('/profile/')


    return render(request,'profile.html',{'obj':obj})

