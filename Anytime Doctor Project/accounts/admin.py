from django.contrib import admin
from django.contrib.auth.models import User

class ListingAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","is_staff")

admin.site.unregister(User)
admin.site.register(User,ListingAdmin)    