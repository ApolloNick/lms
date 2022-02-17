from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, UpdateView
from accounts.forms import AccountRegisterForm, AccountProfileForm


class AccountRegister(CreateView):
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegisterForm


class AccountLogin(LoginView):
    template_name = 'accounts/login.html'


class AccountEdit(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')
    form_class = AccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user


class AccountChangePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "accounts/password_change.html"

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
