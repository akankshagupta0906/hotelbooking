from django.db import models
from HotelBooking.models import UserProfile
from superuser.models import Hotel
from superuser.models import City
from datetime import date



class Bookinghotel(models.Model):
    user= models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    booking_id=models.CharField(max_length=100, default="0")
    total_amt = models.IntegerField(default=0)
    amtstatus = models.IntegerField(default=0)
    start_day=models.CharField(max_length=20,default=30-6-2021)
    end_day=models.CharField(max_length=20,default=30-6-2021)
    booked_on=models.DateTimeField(auto_now=True)
    roomqty = models.IntegerField(default=0)
    guests = models.IntegerField(default=0)

class Cancel(models.Model):
    booking_id = models.CharField(max_length=50)
    reason = models.CharField(max_length=30)
    canceldate = models.DateField(auto_now=True)
    hotel= models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    
class review(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
