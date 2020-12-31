from django.shortcuts import render
from django.http import HttpResponse
from .models import doctor

def doclist(request):

    doctors=doctor.objects.all()

    context = {
        "doctors":doctors
    }

    return render(request,"doctors/doctors.html", context)

def docprofile(request):
    return render(request,"doctors/docprofile.html")    

