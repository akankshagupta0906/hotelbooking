from django.shortcuts import render,redirect
from HotelBooking.models import UserProfile
from superuser.models import Hotel,HotelImage,Manager,Facility,Link,Imagecat
from django.contrib.auth.models import User
from user.models import Bookinghotel


def home(request):
    uobj=User.objects.get(username=request.user)
    mobj=Manager.objects.get(user=uobj)
    hotel=mobj.hotel.hotel_name
    return render(request,"manager.html",{'hotel':hotel})

def image(request):
    icats = Imagecat.objects.all()
    if request.method == "POST":
        img1=request.FILES["image1"]
        img2=request.FILES["image2"]
        img3=request.FILES["image3"]
        cat=request.POST.getlist("imagecat")
        user=User.objects.get(username=request.user)
        m=Manager.objects.get(user=user)
        hobj=Hotel.objects.get(id=m.hotel.id)
        
        li=[img1,img2,img3]
        count=0
        for i in li:
            icat = Imagecat.objects.get(id=cat[count])
            iobj=HotelImage(img=i,hotel=hobj,categoty=icat)
            iobj.save()
            count+=1
        return redirect('/manager/image/')
    return render(request,"image.html",{'cat':icats})


def link1(request):
    lin =Link.objects.all()
    if request.method=="POST":
        lin=request.POST['link']
        m=Manager.objects.get(user=request.user)
        hobj=Hotel.objects.get(id=m.hotel.id)
        lobj=Link(link_img=lin,hotel=hobj)
        lobj.save()
        return redirect('/manager/link/')
        
    return render(request,"link.html",{'lin':lin})
# Create your views here.
def fac(request):
    if request.method=="POST":
        fac1=request.POST["details1"]
        fac2=request.POST["details2"]
        fac3=request.POST["details3"]
        fac4=request.POST["details4"]
        fac5=request.POST["details5"]
        m=Manager.objects.get(user=request.user)
        hobj=Hotel.objects.get(id=m.hotel.id)
        dic=[fac1,fac2,fac3,fac4,fac5]
        for i in dic:
            dobj=Facility(dic=i,hotel=hobj)
            dobj.save()
        return redirect('/manager/fac/')
    return render(request,"facility.html")

def booking(request):
    user=UserProfile.objects.get(user__username = request.user)
    mobj=Manager.objects.get(user=user.user.id)
    hobj=Hotel.objects.get(id=mobj.hotel.id)
    bobj=Bookinghotel.objects.filter(hotel=hobj)
    return render(request,'booked.html',{'bobj':bobj})

def update(request,id):
    book=Bookinghotel.objects.get(id=id)
    hotel1=Hotel.objects.get(id=book.hotel.id)
    hotel=Hotel.objects.filter(id=book.hotel.id)
    room=int(hotel1.total_rooms) + int(book.roomqty)
    hotel.update(total_rooms=room)
    bok=Bookinghotel.objects.filter(id=id)
    bok.delete()
    return redirect('/manager/booking/')
