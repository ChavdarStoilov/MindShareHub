from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomCreateForm, CustomLoginForm

class MyLoginView(generic.FormView):
    form_class = CustomLoginForm
    template_name = 'auth/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home_page')
    
    
class MyLogoutView(LogoutView):
    pass


class MyCreationView(generic.CreateView):
    form_class = CustomCreateForm
    template_name = 'auth/register.html'