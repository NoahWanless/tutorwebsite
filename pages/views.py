from django.shortcuts import render
from django.views.generic import TemplateView
from .models import tutors

class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutors'] = tutors.objects.all()
        return context
