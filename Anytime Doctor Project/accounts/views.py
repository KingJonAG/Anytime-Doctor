from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from accounts.models import UserExtra
from appotests.models import appointment_details,test_details
from doctors.models import doctor
from hospitals.models import hospital
# from django.contrib.auth import authenticate, login


def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        password=request.POST["pass"]

        user=auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"pages/index.html")
            # return redirect("home")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")    

    else:    
        return render(request,"accounts/login.html")

def register(request):
    if request.method== "POST":
        first_name=request.POST["fname"]
        last_name=request.POST["lname"]
        email=request.POST["email"]
        contact_no=request.POST["contact"]
        pass1=request.POST["pass"]
        pass2=request.POST["cpass"]

        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.error(request,"This Email is already existed")
                return redirect("register")
            else:
                user=User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=pass1)
                userextra=UserExtra(user=user,contact_no=contact_no)
                user.save()
                userextra.save()
                messages.success(request,"You are now register and can log in")
                return redirect("login")
        else:
            messages.error(request,"passwords are not matching")
            return redirect("register")

    else:    
        return render(request,"accounts/join.html")    


def home(request):
    return render(request,"accounts/index1.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return render(request,"pages/index.html")   

def dashboard(request):

    appointments=appointment_details.objects.all()
    tests=test_details.objects.all()
    doctors=doctor.objects.all()

    context={
        "appointments":appointments,
        "tests":tests,
        "doctors":doctors
    }

    return render(request,"accounts/dashboard.html",context)             