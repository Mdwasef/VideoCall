from .views import registration,login,logout,dashboard,videocall,joinroom,home
from django.urls import path


urlpatterns=[
path('',home,name='home'),
path('register/',registration ,name='register'),
path('login/',login,name='login'),
path('logout/',login,name='logout'),
path('dashboard/',dashboard,name='dashboard'),
path('video-call/',videocall,name='video-call'),
path('join/',joinroom,name='join'),

]