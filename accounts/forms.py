from django.contrib.auth.forms import UserCreationForm
from pages.models import tutors
from django import forms
from django.contrib.auth import get_user_model



class TutorSignUp(UserCreationForm):
    #first_name = forms.CharField(max_length=20)
    #last_name = forms.CharField(max_length=20)
    #email = forms.EmailField()
    #username
    #password.      both these automatically are there
    class Meta: #get_user_model()
        model = tutors
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','days_tutor_for','classes_tutor_for' )
        help_texts = {
            'username': None,
        }
