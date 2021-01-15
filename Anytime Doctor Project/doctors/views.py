from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import doctor

def doclist(request):

    doctors=doctor.objects.all()

    context = {
        "doctors":doctors
    }

    return render(request,"doctors/doctors.html", context)

def docprofile(request, doc_id):
    doctor_p=get_object_or_404(doctor,pk=doc_id)

    context = {
        "doctor_p":doctor_p
    }

    return render(request,"doctors/docprofile.html",context)    

def doclist1(request):

    doctors=doctor.objects.all()

    context = {
        "doctors":doctors
    }

    return render(request,"doctors/available_doc.html", context)

def doclist2(request):

    doctors=doctor.objects.all()

    context = {
        "doctors":doctors
    }

    return render(request,"doctors/find_doc.html", context)    