from ..rest_api.models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields= (
            "avatar",
            "first_name",
            "last_name",
            "email",
            "desc",
            "status",
        )