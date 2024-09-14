# middlewares.py
from django.shortcuts import redirect

def auth(get_response):
    def middleware(request):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if not authenticated
        response = get_response(request)
        return response
    return middleware
