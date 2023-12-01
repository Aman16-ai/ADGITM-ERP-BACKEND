from celery import shared_task
from django.core.mail import send_mail
from .models import MaintenanceIssue
from accounts.services.UserService import UserService
@shared_task(bind=True)
def send_email_task(self):
    getAllPendingIssues = MaintenanceIssue.getStatusBasedIssues(status='Pending')   
    if len(getAllPendingIssues):
        userSerivece = UserService()
        subject = "ADGITM ERP Remainder mail for pending Issues"
        maintenanceManagerEmailList = userSerivece.getEmailsofAllMaintenaceManager()
        message = "Pending issues are : \n "
        for i in getAllPendingIssues:
            message += i.description + "\n"
        recipient_list = maintenanceManagerEmailList
        print(f"subject {subject} message {message} recipient_list {recipient_list}")
        send_mail(subject=subject,message=message,from_email='amansaxena6523@gmail.com',recipient_list=recipient_list,fail_silently=True)
        return "Done"
    else:
        return "No Pending Issues"