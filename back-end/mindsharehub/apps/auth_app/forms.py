from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm


USER_MODEL = get_user_model()

class CustomChangeForm(forms.ModelForm):
    
     class Meta:
        model = USER_MODEL
        fields = (
            "username",
            "is_staff",
            "is_active"
        )
        
class CustomCreateForm(BaseUserCreationForm):
    pass