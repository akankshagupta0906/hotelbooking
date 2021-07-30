from django.db import models
from django.contrib.auth.models import User
from HotelBooking.models import UserProfile


class City(models.Model):
    cityname=models.CharField(max_length=20)  

class Category(models.Model):
    cat_name= models.CharField(max_length=30)



class Hotel(models.Model):
    hotel_name= models.CharField(max_length=20)
    hotel_image= models.ImageField(upload_to="hotel_image",blank=True)
    hotel_video = models.FileField(upload_to="vedio/%y",blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    price = models.IntegerField()
    total_rooms = models.IntegerField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    near_by = models.CharField(max_length=100)

class Imagecat(models.Model):
    imagename= models.CharField(max_length=30)

class HotelImage(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    categoty = models.ForeignKey(Imagecat, on_delete=models.CASCADE)
    img= models.ImageField(upload_to="hotel_images",blank=True)

class Manager(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        proimg= models.ImageField(upload_to="profile_image",blank=True)
        usertype = models.CharField(max_length=50)
        mobile = models.CharField(max_length=20)
        address = models.CharField(max_length=100)
        age =models.IntegerField()
        gender = models.CharField(max_length=10)
        hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)


class Link(models.Model):
    link_img=models.CharField(max_length=400)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

class Facility(models.Model):
    dic=models.CharField(max_length=400)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    



   




# Create your models here.
