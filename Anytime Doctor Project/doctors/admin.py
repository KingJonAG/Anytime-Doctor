from django.contrib import admin

from .models import doctor

class ListingAdmin(admin.ModelAdmin):
    list_display=("name","speciality","available_online","available_person")

# admin.site.unregister(doctor)
admin.site.register(doctor,ListingAdmin)
