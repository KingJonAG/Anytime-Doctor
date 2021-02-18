from django.urls import path
from . import views

urlpatterns = [
 path('confirm_appointment/<int:doc_id>', views.confirmAppointment, name="appointment"),
 path('select_test/<int:doc_id>', views.select_test, name="select_test")    
]