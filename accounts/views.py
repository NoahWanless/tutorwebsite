from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #mabye get different one
from .forms import TutorSignUp
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = TutorSignUp #!this is custom 
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"