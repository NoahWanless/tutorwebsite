from django.db import models
from django.urls import reverse


class tutors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    userName = models.ForeignKey( #makes this element a forgin key, ie has to match with primary key of another table
        "auth.User",
        on_delete=models.CASCADE,
    )
    classes_tutor_for = models.JSONField(default=list)
    days_tutor_for = models.JSONField(default=list) # put in whther or not they are good for the that day, 7 entires 
    hours_tutor_for = models.JSONField(default=list) #7 entires and you put int he hours 







    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self): #for this post  reverse the full url name with this objects pk as the primary key in the url 
        return reverse("tutor_detail",kwargs={"pk":self.pk}) 
