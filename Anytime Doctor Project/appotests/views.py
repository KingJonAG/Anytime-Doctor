from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from doctors.models import doctor
from hospitals.models import hospital
from .models import appointment_details,test_details
from django.contrib import messages

def confirmAppointment(request,doc_id):  

    if request.method == "POST":
        date=request.POST["date"]
        time=request.POST["time"]


        appointment=appointment_details(hospital_id=doctor.objects.get(id=doc_id).hospital.id,doctor_id=doc_id,patient_id=request.user.id,date=date,time=time)
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

def select_test(request,hosp_id):

    if request.method == "POST":
        date=request.POST["date"]
        time=request.POST["time"]
        test=request.POST["test"]

        test_sc=test_details(hospital_id=hosp_id,patient_id=request.user.id,date=date,time=time,test=test)
        test_sc.save()
        messages.success(request,"Test appointment placed")
        return redirect("dashboard")  
    else:
        hosp_p=get_object_or_404(hospital,pk=hosp_id)

        context = {
            "hosp_p":hosp_p
        }

    return render(request,"appotests/select_test.html",context)

