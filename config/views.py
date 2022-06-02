from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class LoginLandingView(TemplateView):
    template_name = 'login_landing.html'

class LogoutLandingView(TemplateView):
    template_name = 'logout_landing.html'