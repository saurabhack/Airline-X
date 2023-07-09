from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('Booking',views.Booking,name='booking'),
    path('contactus',views.contactus,name='contactus'),
    path('manageflights',views.manageflights,name='manageflights'),
    path('user',views.user,name='user'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('payment',views.payment,name='payment')
]