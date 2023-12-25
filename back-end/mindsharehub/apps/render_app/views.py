from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'main/home.html'
    login_url = reverse_lazy('login_page')