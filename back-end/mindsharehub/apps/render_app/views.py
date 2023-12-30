from django.db.models import Q
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from django.shortcuts import redirect
from ..rest_api.models import UserProfile, Posts, UsersFirendsList
from .forms import UserProfileForm, PostForms
from django.utils.translation import gettext as _


class HomePage(LoginRequiredMixin, generic.ListView):
    template_name = 'main/home.html'
    login_url = reverse_lazy('login_page')
    model = Posts
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Posts.objects.filter(
            Q(user_id__in = [pk.user_id.pk for pk in UsersFirendsList.objects.get(user_id = self.request.user.pk).friends.all()]) |
            Q(user_id =self.request.user.pk)
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['user_friends'] = UsersFirendsList.objects.get(user_id = self.request.user.pk).friends.all()

        return context

    def post(self, request):
        form = PostForms({
            "post": request.POST['new-post'],
            "user_id": UserProfile.objects.get(user_id = self.request.user.pk)
        })


        if form.is_valid():
            form.save()

        return redirect(reverse_lazy('home_page'))
    
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