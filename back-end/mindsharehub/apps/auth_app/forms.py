from django import forms
from django.contrib.auth import get_user_model, forms as auth_forms
from ..rest_api.models import UserProfile

USER_MODEL = get_user_model()

class CustomChangeForm(forms.ModelForm):
    
     class Meta:
        model = USER_MODEL
        fields = (
            "username",
            "is_staff",
            "is_active"
        )
        
        
class CustomCreateForm(auth_forms.UserCreationForm):
    
    first_name = forms.CharField(

    )
    last_name = forms.CharField(

    )
    email = forms.EmailField(

    )
        
    class Meta:
        model = USER_MODEL
        fields = [
            USER_MODEL.USERNAME_FIELD,
            'password1',
            'password2',
            "first_name",
            "last_name",
            "email",
        ]
        
    