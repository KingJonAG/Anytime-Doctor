from django.shortcuts import render,redirect
from django.contrib import messages

def login(request):
    if request.method == "POST":
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
            return render(request,"accounts/join.html")
        else:
            messages.error(request,"passwords not matching")
            return render(request,"accounts/join.html")

    else:    
        return render(request,"accounts/join.html")    