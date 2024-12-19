from django.db import models
from django.contrib.auth.models import User

from a_messageboard.models import MessageBoard

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_board = models.ForeignKey(MessageBoard, on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)  # Automatically set the current time

