from ..rest_api.models import UserProfile, Posts
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


class PostForms(forms.ModelForm):

    class Meta:
        model = Posts
        fields='__all__'