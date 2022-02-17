from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = "accounts/password_change.html"
