from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreation,CustomUserChange
from .models import CustomUser

class SignUpView(CreateView):
    """useing build in calss creat view and adding custom form"""
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileUpdateView(UpdateView):
    """simple profile user"""
    model = CustomUser
    form_class = CustomUserChange
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        # cheking current user request 
        return self.request.user
    
    def form_valid(self, form):
        # updating user picture
        picture = self.request.FILES.get('picture')
        # only update the picture if a new one is provided
        if picture:
            form.instance.picture = self.request.FILES.get('picture')
        return super().form_valid(form)