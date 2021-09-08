from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        name=request.user.get_full_name()
        print(name)
        context={'message':'Hello, '+ name}
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

    return render(request,'index.html')

def about(request):
    if request.user.is_authenticated:
        name=request.user.get_full_name()
        print(name)
        context={'message':'Hello, '+ name}
        return render(request,'about.html',context)
    else:
        return render(request,'about.html')
    return render(request,'about.html')

def courses(request):
    if request.user.is_authenticated:
        name=request.user.get_full_name()
        print(name)
        context={'message':'Hello, '+ name}
        return render(request,'courses.html',context)
    else:
        return render(request,'courses.html')
    return render(request,'courses.html')

def contact(request):
    if request.user.is_authenticated:
        name=request.user.get_full_name()
        print(name)
        context={'message':'Hello, '+ name}
        return render(request,'contact.html',context)
    else:
        return render(request,'contact.html')
    return render(request,'contact.html')

def course_single(request):
    if request.user.is_authenticated:
        name=request.user.get_full_name()
        print(name)
        context={'message':'Hello, '+ name}
        return render(request,'powershell.html',context)
    else:
        return render(request,'powershell.html')
    return render(request,'powershell.html')


# login or sigup code 

def login_url(request):
    if request.method =='POST':
        email =request.POST.get("email")
        password = request.POST.get("password")

        

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_authenticated:
                login(request,user)
                name=user.get_full_name()
                print(name)
                context={'message':'Hello, '+ name}
                return render(request,'index.html',context)
            else:
                return render(request,'index.html')
        else:
            context={'message':'Invalid Email id or Password','class':'danger'}
            return render(request,'login.html',context)
    return render(request,'login.html')
            
def register(request):
    context1 = {'message1':'Login has been created','class':'success'}
    if request.method=="POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        password =request.POST.get("password")
        print(email,name,mobile)

        check_user=User.objects.filter(email=email).first()
        check_profile=Profile.objects.filter(mobile=mobile).first()
    
        if check_user or check_profile:
            context={'message':'User already exists','class':'danger'}
            return render(request,'register.html',context)
        else:
            user =User.objects.create_user(username=email,first_name=name,email=email,password=password)
            user.save()
            print("user_created")
            profile = Profile(user=user ,mobile=mobile)
            profile.save()
            print("profile created")
            return render(request,'register.html',context1)
       
        # user=User(email=email ,first_name=name)
        # user.save()
    return render(request,'register.html')