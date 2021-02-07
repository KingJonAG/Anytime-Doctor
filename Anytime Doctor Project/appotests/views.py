from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from doctors.models import doctor
from hospitals.models import hospital
from .models import appointment_details
from django.contrib.auth.models import User,auth
from django.contrib import messages

def confirmAppointment(request,doc_id):  

    if request.method== "POST":
        date=request.POST["date"]
        time=request.POST["time"]

        appointment=appointment_details(patient=User,doctor=doc_id,hospital=doctor.hospital,date=date,time=time)
        appointment.save()
        messages.success(request,"Appointment Placed")
        return redirect("dashboard")
        
    else:
        doctor_p=get_object_or_404(doctor,pk=doc_id)
        hospitals=hospital.objects.all()

        context = {
            "doctor_p":doctor_p,
            "hospitals":hospitals
        }


    return render(request,"appotests/confirm_appointment.html", context)    
