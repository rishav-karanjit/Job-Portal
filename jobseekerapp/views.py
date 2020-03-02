from django.shortcuts import render
from django.views import generic
from recruiterapp.models import *
from jobseekerapp.models import *

# Create your views here.
class DashboardView(generic.TemplateView):
    template_name='Jobseeker/dashboard.html'

class ViewVacancy(generic.ListView):
    model= Vacancy
    template_name='Jobseeker/ViewVacancy.html'
    context_object_name='vacancys'
    def get_queryset(self):
        return Vacancy.objects.all()

def Applyvacancy(request, pk):
    form = VacancyAppliedForm(request.POST or None)
    vacancys = Vacancy.objects.get(id=pk)
    user = request.user   
    vacancy = vacancys
    jseeker = VacancyApply(vacancy=vacancy,user=user)
    jseeker.save()
    return redirect('VacancyStatus') 