from django.urls import path
from . import views
app_name="superuser"

urlpatterns=[
    path('home/',views.home),
    path('add_hotel/',views.add_hotel),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('hoteldel/',views.hoteldel),
    path('delhotel/<int:id>/',views.delhotel,name='delhotel'),
    path('list_M/',views.list_M),
    path('all_booking/',views.all_booking),
    path('all_user/',views.all_user)
    
    
    ]