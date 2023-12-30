from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomCreateForm, CustomLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

class MyLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'auth/login.html'

    
@login_required
def my_logout(request):
    logout(request)
    return redirect(reverse_lazy('home_page'))



class MyCreationView(generic.CreateView):
    form_class = CustomCreateForm
    template_name = 'auth/register.html'
