from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        
        check_profile=Profile.objects.filter(mobile=mobile).first()
        check_user=User.objects.filter(email=email).first()
        if check_user or check_profile:
            context = {'message':'User already exits','class':'danger'}
            return render(request,'register.html',context)

        user = User(email=email,first_name=name)
        user.save()
    return render(request,'register.html')