from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('home/',views.home),
    path('hotel/',views.hotel),
    path('details/<int:id>/',views.details,name='details'),
    
    path('profile/',views.profile,name='profile'),
    path('booking/<int:id>/',views.booking,name='booking'),
    path('all_booking/',views.all_booking),
    path('cancel/<int:id>/',views.cancel,name='cancel'),
    path('review1/<int:id>/',views.review,name='review')
    
    
    
    
]