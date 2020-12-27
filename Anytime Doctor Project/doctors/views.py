from django.shortcuts import render
from django.http import HttpResponse

def doclist(request):
    return render(request,"doctors/doctors.html")

def docprofile(request):
    return render(request,"doctors/docprofile.html")    

