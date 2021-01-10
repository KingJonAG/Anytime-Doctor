from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_list, name="hospital_list"),
    path('<int:hosp_id>', views.hospital_profile, name="hospital_profile")
]