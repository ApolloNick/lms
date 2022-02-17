from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from accounts.views import AccountRegister, AccountLogin, AccountEdit

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('profile', AccountEdit.as_view(), name='profile'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    path('password/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    path('password/', PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    ]
