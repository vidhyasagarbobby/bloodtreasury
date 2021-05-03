from django.contrib import admin
from hospital.models import Hospital

class HospitalAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Hospital, HospitalAdmin)