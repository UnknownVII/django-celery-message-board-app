from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from celery import shared_task
from .models import *

@shared_task(name='email_notification')
def send_email_task(subject, body, emailAddress, currentUserEmail):
      # Exclude current user and ensure email is not sent twice on the same day
      if emailAddress == currentUserEmail:
            return f"Skipped sending email to {emailAddress} (current user)"

      if SentEmailLog.objects.filter(recipient=emailAddress, subject=subject, sent_date=datetime.today()).exists():
            return f"Email to {emailAddress} with subject '{subject}' already sent today."

      email = EmailMessage(subject, body, to=[emailAddress])
      email.send()

      # Log the sent email
      SentEmailLog.objects.create(recipient=emailAddress, subject=subject)
      return f"Email sent to {emailAddress}"

@shared_task(name='monthly_newsletter')
def send_newsletter():
        subject = "Your Monthly Newsletter"
        subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
              profile__newsletter_subscribed=True
        )

        for subscriber in subscribers:
              body = render_to_string('a_messageboard/newsletter.html', {
                    'name': subscriber.profile.name,
                    'link1': 'https://3.104.175.231:8445/messageboard',
                    'link2': 'https://3.104.175.231:8445/messageboard',
                    'webinar_date': 'December 15th, 2024',
                    'message_board_link': 'https://3.104.175.231:8445/messageboard',
                    'unsubscribe_link': f'https://3.104.175.231:8445/profile/settings'
                }
            )
              email = EmailMessage(subject, body, to=[subscriber.email])
              email.content_subtype = "html"
              email.send()
            
        current_month = datetime.now().strftime('%B')
        subscriber_count = subscribers.count()
        return f'{current_month} Newsletters to {subscriber_count} subs'