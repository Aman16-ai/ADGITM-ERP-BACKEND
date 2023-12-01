
from ..tasks import send_email_task
class EmailService:

    def __init__(self,subject,recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list

    def sendRegistrationEmail(self,username,password):
        message = f"You are successfully register in ADGITM_ERP\n Username : {username} Password {password}"
        print("running email service message",message)
        send_email_task.delay(self.subject,message,self.recipient_list)
        