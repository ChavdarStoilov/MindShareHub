from django.urls import path
from .views import HomePage, UserProfileView

urlpatterns = [
    path('', HomePage.as_view(),  name='home_page'),
    path('profile', UserProfileView.as_view(), name='user_profile_page'),
]
