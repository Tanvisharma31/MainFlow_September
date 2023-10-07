"""rkwebstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from mainapp import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name="login"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('header/', views.header, name="header"),
    path('contactus/', views.contactus, name="ContactUs"),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset/password_reset_form.html"),
         name='password_reset'),
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset/password_reset_mail_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset/new_password.html"),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset/password_reset_complete.html"),
         name='password_reset_complete'),
]
