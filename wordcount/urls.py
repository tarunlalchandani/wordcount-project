from django.urls import path
from . import views
urlpatterns = [
    #here we can direct user and for that we will make views.py
    path('',views.homepage,name = 'home'),#to send back information
    path('count/',views.count,name = 'count'),
    path('about/',views.about,name = 'about'),
]
