from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

class HomePageView(TemplateView):
    """simple home page view"""
    template_name = 'home.html'
    
class ProfilePageView(LoginRequiredMixin,TemplateView):
    """simple profile page view with login-requ.."""
    template_name = 'profile.html'


def logout_user(request):
    # setting a custom logout
    logout(request)
    return redirect('home')