from django.db import models

class hospital(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    contact_no=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    # available_tests=
