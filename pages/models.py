from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
#models.Model
DAY_CHOICES = [
        ('1','Monday'),
        ('2','Tuesday'),
        ('3','Wednesday'),
        ('4','Thrusday'),
        ('5','Friday'),
        ('6','Saturday'),
        ('7','Sunday'),
    ]

HOURS_CHOICE = [
    ('1','8am-9am'),
    ('2','9am-10am'),
    ('3','10am-11am'),
    ('4','11am-12am'),
    ('5','12am-1pm'),
    ('6','1pm-2pm'),
    ('7','3pm-4pm'),
    ('8','4pm-5pm'),
    ('9','5pm-6pm'),
]
class tutors(get_user_model()):
    
    #username = models.ForeignKey( #makes this element a forgin key, ie has to match with primary key of another table
    #    "auth.User",
    #    on_delete=models.CASCADE,
    #)
    
    
    
    hours_tutor_for = models.JSONField(default=list) #7 entires and you put int he hours 
    
    days_tutor_for = MultiSelectField(choices=DAY_CHOICES, min_choices=1, max_choices=7)
    #days_tutor_for = models.CharField(max_length=7,choices=DAY_CHOICES,default='1')
    CLASS_CHOICES = [
        ('CSCI150','CSCI150'),
        ('CSCI151','CSCI151'),
        ('CSCI152','CSCI152'),
        ('CSCI258','CSCI258'),
        ('CSCI340','CSCI340'),
        ('CSCI447','CSCI447'),
    ]
    classes_tutor_for = MultiSelectField(choices=CLASS_CHOICES, min_choices=1, max_choices=6)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self): #for this post  reverse the full url name with this objects pk as the primary key in the url 
        return reverse("tutor_detail",kwargs={"pk":self.pk}) 




#class hours_model(models.Model):
    #day = models.ForeignKey(
    #    tutors,
    ##   on_delete=models.CASCADE,
    #)
    
 #   hours = MultiSelectField(choices=HOURS_CHOICE, min_choices=1, max_choices=9)

    
