from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HotelBooking.models import UserProfile
from django.contrib.auth.hashers import make_password
from .models import City,Category,Hotel,Manager,HotelImage,Link,Facility
from user.models import Bookinghotel




# Create your views here.
def home(request):
    return render(request,"superuser.html")

def add_hotel(request):
    ctobjs=City.objects.all()
    catobjs=Category.objects.all()
    if request.method=="POST":
        nm=request.POST["hname"]
        hm=request.FILES["himage"]
        hv=request.FILES["hvideo"]
        city=request.POST["city"]
        address = request.POST["hadd"]

        mob1 = request.POST["h_mobile"]
        cat=request.POST["category"]
        price= request.POST["price"]
        room = request.POST["totalroom"]
        near_by = request.POST["nearby"]
        
        
        cobj= Category.objects.get(id=cat)
        ctobj = City.objects.get(id=city)
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
        
        

        hobj=Hotel(hotel_name=nm,hotel_image=hm,hotel_video=hv,city=ctobj,address=address,mobile=mob1,price=price,total_rooms=room,cat=cobj,near_by=near_by)
        hobj.save()
       
        obj=User(first_name=fn,last_name=ln,username=un,email=email,password=make_password(pwd))
        obj.save()
        uobj=UserProfile(user=obj,proimg=image,age=age,address=add,mobile=mobile,gender=gen,usertype='manager')
        uobj.save()
        mobj=Manager(user=obj,proimg=image,age=age,address=add,mobile=mobile,gender=gen,usertype='manager',hotel=hobj)
        mobj.save()
        return redirect('/superuser/home/')


    return render(request,"add_hotel.html",{'city':ctobjs,'cat':catobjs})
def profile(request,id):
    
    return render(request,"profile.html")
def profile_update(request):
    uobj=UserProfile.objects.filter(user__username=request.user)
    uobj.update()

    return redirect('/superuser/profile/')
def hoteldel(request):
        c1 = Hotel.objects.all()
        if request.method=='POST':
            search=request.POST['search']
            print(search)
            
            c=[]
            for i in c1:
                if search in i.hotel_name:
                    c.append(i)
               
            return render (request,"del_hotel.html",{'hot':c})
                    
        return render (request,"del_hotel.html",{'hot':c1})
def delhotel(request,id):
    c = Hotel.objects.get(id=id)
    m= Manager.objects.get(hotel=c)
    us=m.user
    m.delete()
    uobj = UserProfile.objects.get(user=us)
    uobj.delete()
    img= HotelImage.objects.filter(hotel=c)
    for i in img:
        im=HotelImage.objects.get(id=i.id)
        im.delete()
    link = Link.objects.get(hotel=c)
    link.delete()
    fac = Facility.objects.filter(hotel=c)
    for i in fac:
        fa=Facility.objects.get(id=i.id)
        fa.delete()
    c.delete()
    return redirect('/superuser/delhotel/')
def list_M(request):
    mobj=Manager.objects.all()
    return render(request,"allmanager.html",{'mobj':mobj})
def all_booking(request):
    bobj=Bookinghotel.objects.all()
    return render(request,"allmanager.html",{'bobj':bobj})
    
def all_user(request):
    uobj=UserProfile.objects.filter(usertype='user')
    return render(request,"allmanager.html",{'uobj':uobj})
    
            



