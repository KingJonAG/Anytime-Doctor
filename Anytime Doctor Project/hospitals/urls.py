from django.urls import path
from . import views

urlpatterns = [
    path('hospital_list', views.hospital_list, name="hospital_list"),
    path('hospital_profile', views.hospital_profile, name="hospital_profile")
]