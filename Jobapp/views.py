from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import User
from django.views.generic.base import TemplateView
from .form import *
# Create your views here.

class SignUpView(generic.CreateView):
    form_class=Signupform
    template_name='registration/signup.html'
    success_url=reverse_lazy('home')

class HomeView(TemplateView):
    template_name = "home.html"
    
