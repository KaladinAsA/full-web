from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreation(UserCreationForm):
    """adding new filds to forms"""
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'picture',
            'username',
            'email',
            'age',
            
        )
        
class CustomUserChange(UserChangeForm):
    """allowing change to new&custom fileds"""
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'picture',
            'username',
            'email',
            'age',
        )