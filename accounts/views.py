from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from accounts.forms import AccountRegisterForm, UserEditForm, ProfileEditForm


class AccountRegister(CreateView):
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            "Registered successfully"
        )
        return result


class AccountLogin(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f"User {self.request.user.username} logged in successfully"
        )
        return result


class AccountEdit(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)
        return render(
            request,
            'accounts/profile.html',
            context={'user_form': user_form,
                     'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile
        user_form = UserEditForm(instance=user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Account edited successfully")
            return redirect(reverse('accounts:profile'))
        return render(
            request,
            'accounts/profile.html',
            context={'user_form': user_form,
                     'profile_form': profile_form})

    def put(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AccountChangePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = "accounts/password_change.html"
