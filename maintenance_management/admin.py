from django.contrib import admin
from .models import MaintenanceIssue,MaintenanceType
# Register your models here.
admin.site.register((MaintenanceIssue,MaintenanceType))