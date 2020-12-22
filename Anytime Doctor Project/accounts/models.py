from django.db import models
from django.contrib.auth.models import User

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    contact_no = models.CharField(max_length=20)


