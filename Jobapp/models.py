from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    role=models.CharField(choices=(
        ('R','Recruiter'),
        ('J','Jobseeker'),
    ),blank = False,max_length=1,default='R')
    avatar=models.ImageField(upload_to='images/')
    Mobile_Number=models.CharField(max_length=10)
    
    def __str__(self):
        return(self.email)
        
