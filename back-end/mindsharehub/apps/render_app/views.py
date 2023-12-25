from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from ..rest_api.models import UserProfile
from .forms import UserProfileForm
from django.utils.translation import gettext as _


class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'main/home.html'
    login_url = reverse_lazy('login_page')
    
    
class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'main/user_profile.html'
    queryset = UserProfile.objects.all()
    form_class = UserProfileForm
    success_url = reverse_lazy('home_page')
        
    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.request.user.pk
        if pk is not None:
            queryset = queryset.filter(user_id=pk)

        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj