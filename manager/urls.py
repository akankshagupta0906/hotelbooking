from django.urls import path
from . import views
app_name="manager"


urlpatterns=[
    path('home/',views.home),
    path('image/',views.image),
    path('link/',views.link1),
    path('fac/',views.fac),
    path('booking/',views.booking,name='booking'),
    path('update/<int:id>/',views.update,name='update')

]