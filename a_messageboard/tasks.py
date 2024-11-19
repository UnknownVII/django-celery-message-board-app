from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from celery import shared_task
from .models import *

@shared_task(name='email_notification')
def send_email_task(subject, body, emailAddress):
    email = EmailMessage(subject, body, to=[emailAddress])
    email.send()
    return emailAddress

@shared_task(name='monthly_newsletter')
def send_newsletter():
        subject = "Your Monthly Newsletter"
        subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
              profile__newsletter_subscribed=True
        )

        for subscriber in subscribers:
              body = render_to_string('a_messageboard/newsletter.html', {
                    'name': subscriber.profile.name,
                    'link1': 'http://127.0.0.1:8000/messageboard',
                    'link2': 'http://127.0.0.1:8000/messageboard',
                    'webinar_date': 'December 15th, 2024',
                    'message_board_link': 'http://127.0.0.1:8000/messageboard',
                    'unsubscribe_link': f'http://127.0.0.1:8000/profile/settings'
                }
            )
              email = EmailMessage(subject, body, to=[subscriber.email])
              email.content_subtype = "html"
              email.send()
            
        current_month = datetime.now().strftime('%B')
        subscriber_count = subscribers.count()
        return f'{current_month} Newsletters to {subscriber_count} subs'