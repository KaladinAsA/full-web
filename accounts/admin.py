from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreation,CustomUserChange
from .models import CustomUser

class CustomAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomUser
    list_display = [
        'email',
        'picture',
        'username',
        'age',
        'is_staff',
    ]
    
    fieldsets = UserAdmin.fieldsets + ((None , {'fields': ('age', 'picture')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None , {'fields': ('age', 'picture')}),)

admin.site.register(CustomUser,CustomAdmin)