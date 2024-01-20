from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ProfilePageView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'


def logout_user(request):
    logout(request)
    return redirect('home')