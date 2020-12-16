from django.shortcuts import render,redirect
from django.contrib import messages

def login(request):
    if request.method == "POST":
        return redirect("login")
    else:    
        return render(request,"accounts/login.html")

def register(request):
    if request.method== "POST":
        return redirect("register")
    return render(request,"accounts/join.html")    