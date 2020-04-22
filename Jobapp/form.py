from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','first_name','last_name','role','avatar','Mobile_Number','profession')