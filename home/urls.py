from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("",index,name="home"),
    path("about",about,name="about"),
    path("courses",courses,name="courses"),
    path("contact",contact,name="contact"),
    path("courses_single",course_single,name='course_single'),
    path("login",login_url,name='login'),
    path('register',register,name='register'),

]

