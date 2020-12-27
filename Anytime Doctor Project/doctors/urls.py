from django.urls import path
from . import views

urlpatterns = [
    path('doclist', views.doclist, name="doclist"),
    path('docprofile', views.docprofile, name="docprofile")
]