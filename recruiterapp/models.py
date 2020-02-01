from django.db import models
from Jobapp.models import *
from .choices import *
from datetime import  datetime
from tinymce.models import HTMLField
# Create your models here.
class recruiterprofile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    Gender=models.IntegerField(choices=Gender_choices,default=1)
    currentcompany=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    resume = models.FileField(upload_to="File/",blank=True)

    def __str__(self):
        return(self.currentcompany)
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