from django.shortcuts import render
from django.views import generic
from recruiterapp.models import *
# Create your views here.
class DashboardView(generic.TemplateView):
    template_name='Jobseeker/dashboard.html'
class ViewVacancy(generic.ListView):
    model= Vacancy
    template_name='Jobseeker/ViewVacancy.html'
    context_object_name='vacancys'
    def get_queryset(self):
        return Vacancy.objects.all()