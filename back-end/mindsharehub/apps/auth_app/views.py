from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    template_name = 'auth/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home_page')
    
    
class MyLogoutView(LogoutView):
    pass