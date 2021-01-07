from django.urls import path
from . import views

urlpatterns = [
    path('', views.doclist, name="doclist"),
    path('<int:doc_id>', views.docprofile, name="docprofile")
]