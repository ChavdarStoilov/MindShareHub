from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from .forms import CustomChangeForm, CustomCreateForm

@admin.register(Users)
class AdminUsers(UserAdmin):
    list_display = [
        'username',
        'is_staff',
        'is_active',
        'date_joined',
        'date_modified',
    ]
    
    readonly_fields = (
        'date_joined',
        'date_modified',
    )
    
    form = CustomChangeForm
    add_form = CustomCreateForm
    
    fieldsets = (
        (
            None, 
            {
                "fields": ("username", "is_staff", "is_active", "groups",)
            }
        ),
    )
    
    
    list_per_page = 20
    