from django.urls import path
from . import views

urlpatterns = [
    path('', views.doclist, name="doclist"),
    path('<int:doc_id>', views.docprofile, name="docprofile"),
    path('available_doc_online', views.doclist1, name="doclist1"),
    path('available_doc_offline', views.doclist2, name="doclist2"),
    path('confirm_appointment/<int:doc_id>', views.confirmAppointment, name="appointment"),
]