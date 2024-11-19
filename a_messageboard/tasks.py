from django.core.mail import EmailMessage
from celery import shared_task

@shared_task(name='email_notification')
def send_email_task(subject, body, emailAddress):
    email = EmailMessage(subject, body, to=[emailAddress])
    email.send()
    return emailAddress
