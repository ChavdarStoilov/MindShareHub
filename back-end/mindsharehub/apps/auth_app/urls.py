from django.urls import path
from .views import MyLoginView, MyCreationView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name="login_page"),
    path('register/', MyCreationView.as_view(), name="register_page")
    
]
