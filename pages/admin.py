from django.contrib import admin
from .models import tutors
#admin.site.register(tutors)
# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "classes_tutor_for",
    )
admin.site.register(tutors,TutorAdmin)