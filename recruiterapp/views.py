from django.shortcuts import render,redirect
from django.views import generic
from .models import *


# Create your views here.
class DashboardView(generic.TemplateView):
    template_name='dashboard.html'
class PostVacancy(generic.CreateView):
    model= Vacancy
    template_name='jseeker_postVacancy.html'
    fields=['company','jobcategory','title','deadline','description']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('Postvacancy')

class ViewVacancy(generic.ListView):
    model= Vacancy
    template_name='ViewVacancy.html'
    context_object_name='vacancys'
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id is None:
            return []
        return Vacancy.objects.filter(user=self.request.user)

class RecruiterProfileView(generic.ListView):
    model=User
    template_name='RecruiterProfile.html'

    def get_context_data(self, **kwargs):
        ctx = super(RecruiterProfileView, self).get_context_data(**kwargs)
        ctx['recruiterprofile'] = recruiterprofile.objects.filter(user=self.request.user)
        return ctx
class RecruiterGDetailsUpdateView(generic.UpdateView):
    model=recruiterprofile
    template_name='RecruiterDetailsUpdateView.html'
    fields=['Gender','currentcompany','profession','resume']
    def form_valid(self,form):
        instance=form.save()
        return redirect('Recruiterprofile')

class RecruiterGDetailsCreateView(generic.CreateView):
    model=recruiterprofile
    template_name='RecruiterDetailsUpdateView.html'
    fields=['Gender','currentcompany','profession','resume']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        instance.save()
        return redirect('Recruiterprofile')