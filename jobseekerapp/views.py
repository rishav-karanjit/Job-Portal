from django.shortcuts import render,redirect
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

class jseekerprofile(generic.ListView):
    model=JseekerProfile
    template_name='Jobseeker/jprofile.html'
    context_object_name='profiles'
    def get_queryset(self):
        print(JseekerProfile.objects.filter(user=self.request.user))
        return JseekerProfile.objects.filter(user=self.request.user)

class jaddskills(generic.CreateView):
    model= JseekerSkill
    template_name='Jobseeker/JAddSkill.html'
    fields=['skill']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        a=instance.id
        return redirect('addproskills',a)

class jaddedu(generic.CreateView):
    model= JseekerEdu
    template_name='Jobseeker/JAddedu.html'
    fields=['institute','degree','field_of_study','date_started','date_ended']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        a=instance.id
        return redirect('addproedu',a)

def Applyvacancy(request, pk):
    vacancys = Vacancy.objects.get(id=pk)
    user = request.user   
    vacancy = vacancys
    jseeker = VacancyApply(vacancy=vacancy,user=user)
    jseeker.save()
    return redirect('VacancyStatus') 

def JobProfileUpdate(request,pk):
    skill=JseekerSkill.objects.get(id=pk)
    user=request.user.id
    j=JseekerProfile.objects.create(user_id=user)
    j.skills.add(skill.id)
    j.save()
    return redirect('JProfile')

def JobProeduUpdate(request,pk):
    edu=JseekerEdu.objects.get(id=pk)
    user=request.user.id
    j=JseekerProfile.objects.create(user_id=user)
    j.education.add(edu.id)
    j.save()
    return redirect('JProfile')

def SkillsDeleteView(request,pk):
    profileobj = JseekerProfile.objects.get(skills=pk)
    skillobj = JseekerSkill.objects.get(id=pk)
    profileobj.delete()
    skillobj.delete()
    return redirect('JProfile')
    #return redirect('JProfile')