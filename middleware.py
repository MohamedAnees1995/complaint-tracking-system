from django.utils.cache import add_never_cache_headers
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class UserRedirectionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is logged in and has a session
        if request.session.get('loggedIn', False):
            user_role = request.session.get('user_role')
            if user_role == 'superadmin' and request.path == '/login/':
                return redirect('superadmindashboard')
            elif user_role == 'admin' and request.path == '/login/':
                return redirect('resolverdashboard')
            elif user_role == 'user' and request.path == '/login/':
                return redirect('userdashboard')