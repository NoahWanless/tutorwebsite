from django.contrib.auth.forms import UserCreationForm
from pages.models import tutors
from django import forms
from django.contrib.auth import get_user_model


class TutorSignUp(UserCreationForm):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    # email = forms.EmailField()
    # username
    # password.      both these automatically are there
    class Meta:  # get_user_model()
        model = tutors
        """fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','days_tutor_for','classes_tutor_for','hours_tutor_for_mon',
                  'hours_tutor_for_tue','hours_tutor_for_wed','hours_tutor_for_thr','hours_tutor_for_fri','hours_tutor_for_sat',
                  'hours_tutor_for_sun')"""
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "days_tutor_for",
            "classes_tutor_for",
        )
        help_texts = {
            "username": None,
        }


class AccountDetailsForm(forms.ModelForm):
    """Form for updating basic account information"""

    class Meta:
        model = tutors
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class AvailabilityForm(forms.ModelForm):
    """Form for updating availability settings"""

    class Meta:
        model = tutors
        fields = (
            "days_tutor_for",
            "classes_tutor_for",
            "hours_tutor_for_mon",
            "hours_tutor_for_tue",
            "hours_tutor_for_wed",
            "hours_tutor_for_thr",
            "hours_tutor_for_fri",
            "hours_tutor_for_sat",
            "hours_tutor_for_sun",
        )
        widgets = {
            "days_tutor_for": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "classes_tutor_for": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_mon": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_tue": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_wed": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_thr": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_fri": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_sat": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "hours_tutor_for_sun": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
        }


"""
 hours_tutor_for_mon = models.JSONField(blank=True, default=list) 
    hours_tutor_for_tue = models.JSONField(blank=True, default=list) 
    hours_tutor_for_wed = models.JSONField(blank=True, default=list) 
    hours_tutor_for_thr = models.JSONField(blank=True, default=list) 
    hours_tutor_for_fri = models.JSONField(blank=True, default=list) 
    hours_tutor_for_sat = models.JSONField(blank=True, default=list) 
    hours_tutor_for_sun = models.JSONField(blank=True, default=list) 
    """
