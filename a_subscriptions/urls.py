from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/<int:messageboard_id>/<int:user_id>/', views.subscribe, name='subscribe'),
    path('health/', views.health_check, name='health_check'),
]
