from django.db import models
from Jobapp.models import *
from datetime import  datetime
from tinymce.models import HTMLField
# Create your models here.
   
class Vacancy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    jobcategory=models.IntegerField(choices=category_choices)
    title=models.CharField(max_length=50)
    date_added=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    deadline=models.DateField()
    description=HTMLField(blank=True)

    def __str__(self):
        return(self.title)
    
    @property
    def is_past(self):
        return(date.today() < self.deadline)