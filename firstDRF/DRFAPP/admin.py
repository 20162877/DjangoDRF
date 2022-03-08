from django.contrib import admin
from DRFAPP.models import Patient


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'USER_ID', 'TIMESTAMP', 'HEART_RATE', 'RESP_RATE', 'ACTIVITY')


admin.site.register(Patient, PatientAdmin)
