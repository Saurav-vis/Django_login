
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('reset-password/',PasswordResetView.as_view(template_name='authentication/reset-password.html'), name='reset-password'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-done/',PasswordResetDoneView.as_view(), name = 'password_reset_done')
]
