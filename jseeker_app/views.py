from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.
class PostVacancy(generic.CreateView):
    model= Vacancy
    template_name='jseeker_postVacancy.html'
    fields=['company','jobcategory','title','deadline','description']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('vacancy')