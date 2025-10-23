from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
#models.Model

class tutors(get_user_model()):
    HOUR_CHOICES = [
        ('7','7-8am'),
        ('8','8-9am'),
        ('9','9-10am'),
        ('10','10-11am'),
        ('11','11-12pm'),
        ('12','12-1pm'),
        ('13','1-2pm'),
        ('14','2-3pm'),
        ('15','3-4pm'),
        ('16','4-5pm'),
        ('17','5-6pm'),
    ]
    #username = models.ForeignKey( #makes this element a forgin key, ie has to match with primary key of another table
    #    "auth.User",
    #    on_delete=models.CASCADE,
    #)
    
    #classes_tutor_for = models.JSONField(default=list)
    
    hours_tutor_for_mon = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_tue = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_wed = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_thr = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_fri = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_sat = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    hours_tutor_for_sun = MultiSelectField(choices=HOUR_CHOICES, min_choices=0, max_choices=11,blank=True)
    
    
    DAY_CHOICES = [
        ('1','Monday'),
        ('2','Tuesday'),
        ('3','Wednesday'),
        ('4','Thrusday'),
        ('5','Friday'),
        ('6','Saturday'),
        ('7','Sunday'),
    ]
    days_tutor_for = MultiSelectField(choices=DAY_CHOICES, min_choices=1, max_choices=7)
    CLASS_CHOICES = [
        ('CSCI150','CSCI150'),
        ('CSCI151','CSCI151'),
        ('CSCI152','CSCI152'),
        ('CSCI258','CSCI258'),
        ('CSCI340','CSCI340'),
        ('CSCI447','CSCI447'),
    ]
    classes_tutor_for = MultiSelectField(choices=CLASS_CHOICES, min_choices=1, max_choices=6)

    def get_days_display(self):
        display_values = dict(self.DAY_CHOICES)
        return [display_values[val] for val in self.days_tutor_for]
    
    def get_hours_mon_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_mon]
    
    def get_hours_tue_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_tue]
    
    def get_hours_wed_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_wed]
    
    def get_hours_thr_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_thr]
    
    def get_hours_fri_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_fri]
    
    def get_hours_sat_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_sat]
    
    def get_hours_sun_display(self):
        display_values = dict(self.HOUR_CHOICES)
        return [display_values[val] for val in self.hours_tutor_for_sun]
    #def __str__(self):
        #return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self): #for this post  reverse the full url name with this objects pk as the primary key in the url 
        return reverse("tutor_detail",kwargs={"pk":self.pk}) 
