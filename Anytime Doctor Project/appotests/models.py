from django.db import models
from django.contrib.auth.models import User
from hospitals.models import hospital
from doctors.models import doctor

class appointment_details(models.Model):
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    doctor = models.ForeignKey(doctor, on_delete=models.DO_NOTHING) 
    hospital = models.ForeignKey(hospital, on_delete=models.DO_NOTHING) 
    date = models.DateField()
    time = models.TimeField()

class test_details(models.Model):
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    test = models.CharField(max_length=200)
    hospital = models.ForeignKey(hospital, on_delete=models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField() 

class video_chat(models.Model):
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)  

    