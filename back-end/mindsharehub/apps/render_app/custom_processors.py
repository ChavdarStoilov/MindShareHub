from ..rest_api.models import UserProfile
from django.contrib.auth import get_user_model

User_Model = get_user_model()


def get_user_profile(request):
    
    try:
        user_profile = UserProfile.objects.get(user_id = request.user.pk)
        return {
            'profile':user_profile
            }
    except:
        return {}