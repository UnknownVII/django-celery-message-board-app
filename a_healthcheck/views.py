from django.http import JsonResponse

def health_check_view(request):
    """
    A basic health check endpoint to ensure the application is up and running.
    """
    return JsonResponse({"status": "ok"}, status=200)