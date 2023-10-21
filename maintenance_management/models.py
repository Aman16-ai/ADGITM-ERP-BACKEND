from django.db import models
from accounts.models import UserAccount
# Create your models here.
maintenance_choices = [
    ('Civil','Civil'),
    ('Water','Water'),
    ('Electric',"Electric")
]
issue_status_choices = [
    ('Pending','Pending'),
    ('Hold','Hold'),
    ('Completed','Completed'),
    ('Rejected','Rejected')
]
class MaintenanceIssue(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True,blank=True)
    maintenanceType = models.CharField(choices=maintenance_choices,max_length=40)
    description = models.TextField()
    status = models.CharField(choices=issue_status_choices,max_length=20,default='Pending')
    timestamp = models.DateTimeField(auto_created=True,auto_now=True,blank=True,null=True)

    def __str__(self) -> str:
        return self.maintenanceType + " " + self.status