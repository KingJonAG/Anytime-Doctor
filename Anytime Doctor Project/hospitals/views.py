from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import hospital

def hospital_list(request):
    hospitals=hospital.objects.all()

    context = {
        "hospitals":hospitals
    }

    return render(request,"hospitals/hospital_list.html", context)

def hospital_profile(request):
    return render(request,"hospitals/hospital.html")      
