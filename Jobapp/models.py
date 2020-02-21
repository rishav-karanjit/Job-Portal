from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from .choices import *
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
    currentcompany=models.CharField(max_length=100,blank=True)
    Gender=models.IntegerField(choices=Gender_choices,default=1)
    profession=models.CharField(max_length=100,blank=True)
    resume = models.FileField(upload_to="File/",blank=True)

    def __str__(self):
        return(self.email)
        
