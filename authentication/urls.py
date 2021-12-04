from .views import (
  SignUpView,
  AccountView,
  PasswordView,
  DeleteAccountView,
  ActivateAccountView
)

from django.urls import path

urlpatterns = [
  path('signup/', SignUpView, name="signup"),
  path('account/', AccountView, name="account"),
  path('password/', PasswordView, name="password"),
  path('delete/', DeleteAccountView, name="delete"),
  path('activate-account/<token>/', ActivateAccountView, name='activate'),
]