from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth

def index(request):
    return render(request,"pages/index.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return render(request,"pages/index.html")        
