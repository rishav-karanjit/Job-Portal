from django.shortcuts import render,redirect
from django.views import generic
from .models import *


# Create your views here.
class DashboardView(generic.TemplateView):
    template_name='Recruiters/dashboard.html'
    
class PostVacancy(generic.CreateView):
    model= Vacancy
    template_name='Recruiters/postVacancy.html'
    fields=['jobcategory','title','deadline','description']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.company=self.request.user.currentcompany
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('Postvacancy')

class ViewVacancy(generic.ListView):
    model= Vacancy
    template_name='Recruiters/ViewVacancy.html'
    context_object_name='vacancys'
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id is None:
            return []
        return Vacancy.objects.filter(user=self.request.user)

class RecruiterProfileView(generic.ListView):
    model=User
    template_name='Recruiters/RecruiterProfile.html'

    def get_context_data(self, **kwargs):
        ctx = super(RecruiterProfileView, self).get_context_data(**kwargs)
        # ctx['recruiterprofile'] = User.objects.filter(user=self.request.user)
        return ctx
class RecruiterDetailsUpdateView(generic.UpdateView):
    model=User
    template_name='Recruiters/RecruiterDetailsUpdateView.html'
    fields=['first_name','last_name','avatar','Mobile_Number','currentcompany','Gender','profession','resume']
    def form_valid(self,form):
        instance=form.save()
        return redirect('Recruiterprofile')

# class RecruiterGDetailsCreateView(generic.CreateView):
#     model=recruiterprofile
#     template_name='Recruiters/RecruiterDetailsUpdateView.html'
#     fields=['Gender','currentcompany','profession','resume']
#     def form_valid(self,form):
#         instance=form.save(commit=False)
#         instance.user=self.request.user
#         instance.save()
#         return redirect('Recruiterprofile')