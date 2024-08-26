from django.urls import path
from apps.accounts.views import HomeView, LoginView, LogoutView, TestView, SignUpView, PrivacyPolicyView
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )


# app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
