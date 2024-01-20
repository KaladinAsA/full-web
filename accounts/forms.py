from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'picture',
            'username',
            'email',
            'age',
            
        )
        
class CustomUserChange(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'picture',
            'username',
            'email',
            'age',
        )