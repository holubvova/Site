import datetime
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from django.core.mail import EmailMultiAlternatives

from Site import settings


def send_maill(email,  message:str, subject:str):
    status = "error"
    list_email=[]
    cc_list_email=[]
    if  (type(email) == list) :
        list_email = list(email)
    else:
        list_email = email


    msg = EmailMultiAlternatives(subject,message, settings.EMAIL_HOST_USER, list_email)
    try:
        msg.send(fail_silently=False)
        # print(email, message, subject)
        status = "success"
    except Exception as e:
        status = f"error{e}"
        print(e)

    return {
        "queue": "email",
        "name": f"{subject}",
        "data": f"{message}",
        "result": f"{status}",
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "recipient": f"{list_email}"
    }