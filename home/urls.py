from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("",index,name="home"),
    path("about",about,name="about"),
    path("courses",courses,name="courses"),
    path("contact",contact,name="contact"),

]

