from django.db import models

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
    # hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING) 

