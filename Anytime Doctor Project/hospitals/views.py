from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import hospital

def hospital_list(request):
    hospitals=hospital.objects.all()

    context = {
        "hospitals":hospitals
    }

    return render(request,"hospitals/hospital_list.html", context)

def hospital_profile(request,hosp_id):

    hosp_p=get_object_or_404(hospital,pk=hosp_id)

    context = {
        "hosp_p":hosp_p
    }

    return render(request,"hospitals/hospital.html",context)      
