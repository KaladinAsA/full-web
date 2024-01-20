from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreation,CustomUserChange
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChange
    # fields = ('username', 'email', 'age', 'picture')
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        form.instance.picture = self.request.FILES.get('picture')
        return super().form_valid(form)