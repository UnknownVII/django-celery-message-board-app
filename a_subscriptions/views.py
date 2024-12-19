from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import a_core
from a_messageboard.models import MessageBoard
from .models import Subscription
from django.http import JsonResponse
from django.contrib.auth.models import User

def subscribe(request, messageboard_id, user_id):
    messageboard = get_object_or_404(MessageBoard, id=messageboard_id)
    user = get_object_or_404(User, id=user_id)
    
    # Add or remove the user from subscribers
    if user in messageboard.subscribers.all():
        messageboard.subscribers.remove(user)
    else:
        messageboard.subscribers.add(user)
    
    # Redirect to the frontend app
    return redirect(f'{a_core.settings.FRONTEND_URL}/messageboard')

def health_check(request):
    return JsonResponse({"status": "ok"})