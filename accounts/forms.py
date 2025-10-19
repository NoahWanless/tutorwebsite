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
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','days_tutor_for','classes_tutor_for','hours_tutor_for_mon',
                  'hours_tutor_for_tue','hours_tutor_for_wed','hours_tutor_for_thr','hours_tutor_for_fri','hours_tutor_for_sat',
                  'hours_tutor_for_sun')
        help_texts = {
            'username': None,
        }

'''
 hours_tutor_for_mon = models.JSONField(blank=True, default=list) 
    hours_tutor_for_tue = models.JSONField(blank=True, default=list) 
    hours_tutor_for_wed = models.JSONField(blank=True, default=list) 
    hours_tutor_for_thr = models.JSONField(blank=True, default=list) 
    hours_tutor_for_fri = models.JSONField(blank=True, default=list) 
    hours_tutor_for_sat = models.JSONField(blank=True, default=list) 
    hours_tutor_for_sun = models.JSONField(blank=True, default=list) 
    '''