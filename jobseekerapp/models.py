from django.db import models
from Jobapp.models import *
from recruiterapp.models import *
from .choices import *

class VacancyApply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vacancy=models.ForeignKey(Vacancy,on_delete=models.CASCADE,related_name="vac")
    applieddate=models.DateField(auto_now=True)
    status=models.IntegerField(choices=status_choices,default=1)
    
class JseekerSkill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill=models.CharField(max_length=50)

class JseekerEdu(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    institute=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    field_of_study=models.CharField(max_length=50)
    date_started=models.DateField(blank=True,null=True)
    date_ended=models.DateField(blank=True,null=True)

class JseekerProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skills=models.ManyToManyField(JseekerSkill)
    education=models.ManyToManyField(JseekerEdu)
    appliedvacancy=models.ManyToManyField(VacancyApply)