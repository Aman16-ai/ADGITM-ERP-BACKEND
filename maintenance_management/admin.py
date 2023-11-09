from django.contrib import admin
from .models import MaintenanceIssue,MaintenanceType,MaintenanceIssueComment
# Register your models here.
admin.site.register((MaintenanceIssue,MaintenanceType,MaintenanceIssueComment))