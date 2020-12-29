from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth

def hospital_list(request):
    return render(request,"hospitals/hospital_list.html")

def hospital_profile(request):
    return render(request,"hospitals/hospital.html")      
