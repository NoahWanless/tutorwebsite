from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from .forms import TutorSignUp, AccountDetailsForm, AvailabilityForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pages.models import tutors
from django.utils.translation import gettext as _

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

@method_decorator(login_required, name='dispatch')
class AccountSettingsView(View):
    def get(self, request):
        tutor_instance, _created = tutors.objects.get_or_create(pk=request.user.pk)
        print(f"Tutor instance: {tutor_instance.pk}, created: {_created}")
        print(f"Days: {tutor_instance.days_tutor_for}")
        print(f"Mon hours: {tutor_instance.hours_tutor_for_mon}")
        account_form = AccountDetailsForm(instance=tutor_instance)
        availability_form = AvailabilityForm(instance=tutor_instance)
        day_field = tutors._meta.get_field('days_tutor_for')
        days_choices = list(day_field.choices)
        hour_field = tutors._meta.get_field('hours_tutor_for_mon')
        hour_choices = list(hour_field.choices)

        def get_label(choices, value):
            for v, label in choices:
                if str(v) == str(value):
                    return label
            return str(value)

        day_key_to_field = {
            '1': 'hours_tutor_for_mon',
            '2': 'hours_tutor_for_tue',
            '3': 'hours_tutor_for_wed',
            '4': 'hours_tutor_for_thr',
            '5': 'hours_tutor_for_fri',
            '6': 'hours_tutor_for_sat',
            '7': 'hours_tutor_for_sun',
        }

        saved_schedule = []
        print(f"Building saved_schedule for tutor {tutor_instance.pk}")
        for day_value, day_label in days_choices:
            field_name = day_key_to_field.get(str(day_value))
            if not field_name:
                continue
            selected_values = getattr(tutor_instance, field_name, []) or []
            print(f"Day {day_value} ({day_label}): {field_name} = {selected_values}")
            if selected_values:
                labels = [get_label(hour_choices, v) for v in selected_values]
                day_data = {
                    'day_value': str(day_value),
                    'day_label': day_label,
                    'hours': labels,
                    'hour_values': selected_values,
                }
                saved_schedule.append(day_data)
                print(f"Added to saved_schedule: {day_data}")
        
        print(f"Final saved_schedule: {saved_schedule}")

        import json
        saved_schedule_json = json.dumps(saved_schedule)
        print(f"Saved schedule JSON: {saved_schedule_json}")
        
        context = {
            'account_form': account_form,
            'availability_form': availability_form,
            'active_section': 'account_details',
            'days_choices': days_choices,
            'hour_choices': hour_choices,
            'saved_schedule': saved_schedule,
            'saved_schedule_json': saved_schedule_json,
        }
        return render(request, 'accounts/settings.html', context)
    
    def post(self, request):
        tutor_instance, _created = tutors.objects.get_or_create(pk=request.user.pk)

        if 'account_details' in request.POST:
            form = AccountDetailsForm(request.POST, instance=tutor_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account details updated successfully!')
                return redirect('settings')
            else:
                availability_form = AvailabilityForm(instance=tutor_instance)
                context = {
                    'account_form': form,
                    'availability_form': availability_form,
                    'active_section': 'account_details'
                }
                return render(request, 'accounts/settings.html', context)
        
        elif 'availability' in request.POST:
            selected_availability_json = request.POST.get('selected_availability', '{}')
            print(f"Received selected_availability_json: {selected_availability_json}")
            if selected_availability_json:
                try:
                    import json
                    selected_availability = json.loads(selected_availability_json)
                    print(f"Parsed selected_availability: {selected_availability}")

                    tutor_instance.hours_tutor_for_mon = []
                    tutor_instance.hours_tutor_for_tue = []
                    tutor_instance.hours_tutor_for_wed = []
                    tutor_instance.hours_tutor_for_thr = []
                    tutor_instance.hours_tutor_for_fri = []
                    tutor_instance.hours_tutor_for_sat = []
                    tutor_instance.hours_tutor_for_sun = []

                    days_with_availability = list(selected_availability.keys())
                    tutor_instance.days_tutor_for = days_with_availability

                    day_to_field = {
                        '1': 'hours_tutor_for_mon',
                        '2': 'hours_tutor_for_tue', 
                        '3': 'hours_tutor_for_wed',
                        '4': 'hours_tutor_for_thr',
                        '5': 'hours_tutor_for_fri',
                        '6': 'hours_tutor_for_sat',
                        '7': 'hours_tutor_for_sun',
                    }
                    
                    for day_value, hours in selected_availability.items():
                        field_name = day_to_field.get(day_value)
                        if field_name:
                            setattr(tutor_instance, field_name, hours)
                    
                    tutor_instance.save()
                    messages.success(request, 'Availability settings updated successfully!')
                    return redirect('settings')
                    
                except (json.JSONDecodeError, ValueError) as e:
                    messages.error(request, f'Error processing availability data: {str(e)}')

            form = AvailabilityForm(request.POST, instance=tutor_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Availability settings updated successfully!')
                return redirect('settings')
            else:
                account_form = AccountDetailsForm(instance=tutor_instance)
                context = {
                    'account_form': account_form,
                    'availability_form': form,
                    'active_section': 'availability',
                    'days_choices': tutors._meta.get_field('days_tutor_for').choices,
                    'hour_choices': tutors._meta.get_field('hours_tutor_for_mon').choices,
                    'saved_schedule': []
                }
                return render(request, 'accounts/settings.html', context)
        
        
        return redirect('settings')