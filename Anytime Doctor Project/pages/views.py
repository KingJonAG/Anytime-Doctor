from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from doctors.models import doctor
from hospitals.models import hospital

def index(request):

    doctors=doctor.objects.all()
    hospitals=hospital.objects.all()

    context = {
        "doctors":doctors[:3],
        "hospitals":hospitals[:3]
    }


    return render(request,"pages/index.html",context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return render(request,"pages/index.html")        
