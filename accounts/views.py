from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from .forms import TutorSignUp
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = TutorSignUp
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Please log in.')
        return response




class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.', extra_tags='logout')
        return redirect('home')

class AccountSettingsView(View):
    def get(self, request):
        return render(request, 'accounts/settings.html')