from django.core.mail import send_mail
from django.conf import settings

class Send_email_handler:
    @staticmethod
    def send_email(user_email:str, title:str, message:str):
        send_mail(subject=title,
		  message=message,
		  from_email=settings.EMAIL_HOST_USER,
		  recipient_list=[user_email])


