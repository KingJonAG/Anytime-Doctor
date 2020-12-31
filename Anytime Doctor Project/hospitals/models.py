from django.db import models

class hospital(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    contact_no=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    blood_count=models.BooleanField(default=False)
    biopsy=models.BooleanField(default=False)
    ecg=models.BooleanField(default=False)
    ct_scan=models.BooleanField(default=False)
    angiogram=models.BooleanField(default=False)
    ultra_sound=models.BooleanField(default=False)
    picture=models.ImageField(upload_to="photos/hospitals/")
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name
