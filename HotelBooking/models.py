from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        proimg= models.ImageField(upload_to="profile_image",blank=True)
        usertype = models.CharField(max_length=50)
        mobile = models.CharField(max_length=20)
        address = models.CharField(max_length=100)
        age =models.IntegerField()
        gender = models.CharField(max_length=10)


