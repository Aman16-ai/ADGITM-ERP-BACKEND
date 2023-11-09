from django.db import models
from accounts.models import UserAccount
from departmenant_managnement.models import Department
# Create your models here.
maintenance_choices = [
    ('Civil','Civil'),
    ('Water','Water'),
    ('Electric',"Electric")
]
issue_status_choices = [
    ('Pending','Pending'),
    ('Progress','Progress'),
    ('Completed','Completed'),
    ('Rejected','Rejected')
]
class MaintenanceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
class MaintenanceIssue(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True,blank=True)
    maintenanceType = models.ForeignKey(MaintenanceType,on_delete=models.SET_NULL,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField()
    status = models.CharField(choices=issue_status_choices,max_length=20,default='Pending')
    created_at = models.DateField(auto_created=True,auto_now=True,blank=True,null=True)

    def __str__(self) -> str:
        return self.maintenanceType.name + " " + self.status
    

class MaintenanceIssueComment(models.Model):
    id = models.AutoField(primary_key=True)
    commented_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    maintenanceIssue = models.ForeignKey(MaintenanceIssue,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.commented_by.username + " " + self.comment
    