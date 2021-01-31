from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from doctors.models import doctor
from hospitals.models import hospital

def confirmAppointment(request,doc_id):    

    doctor_p=get_object_or_404(doctor,pk=doc_id)
    hospitals=hospital.objects.all()

    context = {
        "doctor_p":doctor_p,
        "hospitals":hospitals
    }

    return render(request,"appotests/confirm_appointment.html", context)    
