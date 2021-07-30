from django.shortcuts import render,redirect
from superuser.models import City,Category,Hotel,Manager,HotelImage,Facility,Link
import random 
import datetime
from HotelBooking.models import UserProfile
from .models import Bookinghotel,Cancel,review
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request,"user.html")

def details(request,id):#hotels details
    det=Hotel.objects.get(id=id)

    imgs=HotelImage.objects.filter(hotel=det)
    # limited 4 image in carousel
    count=0
    img=[]
    for i in imgs:
        if count==4:
            break
        else:
            img.append(i)
            count+=1
        
    aobj=Facility.objects.filter(hotel=det)
    lin =Link.objects.filter(hotel=det)
    re = review.objects.filter(hotel__id=det.id)
    bal=[]
    ra=[]
    res=[]
    for i in imgs:
        if i.categoty.imagename=='balcony':
            bal.append(i)
        elif i.categoty.imagename=='room area':
            ra.append(i)
        elif i.categoty.imagename=='resaption area':
            res.append(i)
    user=UserProfile.objects.get(user__username=request.user)
    hobj=Hotel.objects.get(id=id)
    if request.method=="POST":
        rev = request.POST['review']
        robj= review(user=user,hotel=det,review=rev)
        robj.save()
        
    return render(request,"details.html",{'det':det,'imgs':img,'aobj':aobj,'lin':lin,'bal':bal,'ra':ra,'res':res,'re':re})


def hotel(request):#hotel card
    cobj=City.objects.all()
    catobj = Category.objects.all()
    hot = Hotel.objects.all()
    #search by 
    if request.method== "POST":
        ser=request.POST['city']
        
        hot=Hotel.objects.filter(city__id=ser)
        return render(request,"hotel.html",{'cobj':cobj,'catobj':catobj,'hot':hot})
    return render(request,"hotel.html",{'cobj':cobj,'catobj':catobj,'hot':hot})


def profile(request):
    uobj=UserProfile.objects.filter(usertype='user')
    

    return render(request,"profile.html",{'uobj':uobj})

def booking(request,id):#book hotel 
    
        hobj= Hotel.objects.get(id=id)
        uobj=UserProfile.objects.get(user__username=request.user)
        
        
        if request.method=="POST":
            
            
            
            room= request.POST["room"] 
            gue= request.POST["guests"]
            ctobj = City.objects.get(id=hobj.city.id)
            amt= int(hobj.price)*int(room)
            srt_day = request.POST["start_day"]
            end_day = request.POST["end_day"] 
            bid=datetime.date.today()
            rem=random.randint(0,99999)
            y=str(bid).replace("-","").replace(" ","").replace(":","").replace(".","")
            bid2=str(y)+str(rem)
            
            
            book=Bookinghotel(hotel=hobj,city=ctobj,user=uobj,total_amt=amt,start_day=srt_day,end_day=end_day,roomqty=room,booking_id=bid2,guests=gue)
            
            book.save()
           
        
            # update hotels      
            hobjs = Hotel.objects.filter(id=id) #QuerySet(pobj)
            newQty = hobj.total_rooms - int(room)
            hobjs.update(total_rooms=newQty)
             
            return render(request,"booking.html",{'hobj':book})

        return render(request,"bookingdata.html",{'hobj':hobj})
   
    

def hotel_name(request,id):
    #search hotel
    if request.method== "POST":
        ser=request.POST['search']
        hot=hotel.objects.filter(hotel_name=ser)
        return render(request,"hotel.html",{'cobj':cobj,'catobj':catobj,'hot':hot})
    
def all_booking(request):
    user=UserProfile.objects.get(user__username=request.user)
    book =Bookinghotel.objects.filter(user=user)
    return render(request,"book.html",{'book':book})
def cancel(request,id):
    book=Bookinghotel.objects.get(id=id)
    hotel1=Hotel.objects.get(id=book.hotel.id)
    hotel=Hotel.objects.filter(id=book.hotel.id)
    room=int(hotel1.total_rooms) + int(book.roomqty)
    hotel.update(total_rooms=room)
    bok=Bookinghotel.objects.filter(id=id)
    bok.delete()
    return redirect('/user/all_booking/')

def review1(request,id):
    user=UserProfile.objects.get(user__username=request.user)
    hobj=Hotel.objects.get(id=id)
    if method=="POST":
        rev = method.POST['review']
        robj= review(user=user,hotel=hob,review=rev)
        robj.save()
    
    return redirect('/user/details/')