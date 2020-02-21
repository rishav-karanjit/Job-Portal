from django.shortcuts import render

# Create your views here.
class DashboardView():
    pass
class ViewVacancy(generic.ListView):
    model= Vacancy
    template_name='Jobseeker/ViewVacancy.html'
    context_object_name='vacancys'