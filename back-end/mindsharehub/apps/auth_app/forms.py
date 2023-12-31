from typing import Any
from django import forms
from django.contrib.auth import get_user_model, forms as auth_forms
from ..rest_api.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

USER_MODEL = get_user_model()

class CustomChangeForm(forms.ModelForm):
    
    class Meta:
       model = USER_MODEL
       fields = (
           "username",
           "is_staff",
           "is_active"
       )
        
        
class CustomLoginForm(AuthenticationForm):
    pass

class CustomCreateForm(auth_forms.UserCreationForm):
    
    first_name = forms.CharField(
        widget=
            forms.TextInput(
                attrs={
                    'class': 'first-name-field',  
                }
            )
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
        
        
    def save(self, commit=True):
        user=super().save(commit=commit)
        
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        
      
        profile = UserProfile(
            first_name = first_name,
            last_name = last_name,
            email=email,
            user_id=user,
        )
      
        if commit:
            profile.save()
        
        return user
        
    