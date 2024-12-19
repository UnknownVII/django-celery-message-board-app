from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import a_core
from a_messageboard.models import MessageBoard
from .models import Subscription
from django.http import JsonResponse

def subscribe(request, messageboard_id):
    messageboard = get_object_or_404(MessageBoard, id=messageboard_id)
    
    # Add user to the subscribers if they are not already subscribed
    if request.user not in messageboard.subscribers.all():
        messageboard.subscribers.add(request.user)
    else:
        messageboard.subscribers.remove(request.user)

    # Use the setting to redirect to the correct port
    return redirect(f'{a_core.settings.FRONTEND_URL}/messageboard')

def health_check(request):
    return JsonResponse({"status": "ok"})