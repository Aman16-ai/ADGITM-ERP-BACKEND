from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True)
def send_email_task(self,subject,message,recipient_list):
    send_mail(subject,message,'asaxena7531@gmail.com',recipient_list)