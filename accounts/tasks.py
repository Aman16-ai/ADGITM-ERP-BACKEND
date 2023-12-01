from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True)
def send_email_task(self,subject,message,recipient_list):
    print(f"subject {subject} message {message} recipient_list {recipient_list}")
    send_mail(subject=subject,message=message,from_email='amansaxena6523@gmail.com',recipient_list=recipient_list,fail_silently=True)
    return "Done"