from django.db import models
from hospitals.models import hospital

class doctor(models.Model):
    name = models.CharField(max_length=200)
    speciality_choices = [
    ('Family Physician', 'Family Physician'),
    ('Pediatrician', 'Pediatrician'),
    ('Obstetrician/Gynecologist', 'Obstetrician/Gynecologist'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologist', 'Dermatologist')]
    speciality=models.CharField(
        max_length=50,
        choices=speciality_choices,
        default="",)
    hospital = models.ForeignKey(hospital, on_delete=models.DO_NOTHING) 
    email=models.EmailField(max_length=200)
    picture=models.ImageField(upload_to="photos/hospitals/")
    description=models.TextField(blank=True)
    available_online=models.BooleanField(default=False)
    available_person=models.BooleanField(default=False)
    def __str__(self):
        return self.name

