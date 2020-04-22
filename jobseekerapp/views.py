from django.shortcuts import render,redirect
from django.views import generic
from recruiterapp.models import *
from jobseekerapp.models import *
from Jobapp.models import *

# Create your views here.
class DashBoard(generic.ListView):
    model=Vacancy
    template_name='Jobseeker/home.html'
    context_object_name='job'
    def get_queryset(self):
        return Vacancy.objects.filter(jobcategory=self.request.user.profession)
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data['skills_count']=JseekerSkill.objects.filter(user=self.request.user).count()
        data['connection_count']=User.objects.filter(id=self.request.user.id).count()
        data['appliedvacancy']=VacancyApply.objects.filter(user=self.request.user).count()
        return data

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

class AppliedVacancy(generic.ListView):
    model=VacancyApply
    template_name='Jobseeker/appliedvac.html'
    context_object_name='vacancys'
    def get_queryset(self):
        return VacancyApply.objects.filter(user=self.request.user)

def Applyvacancy(request, pk):
    vacancys = Vacancy.objects.get(id=pk)
    user = request.user   
    vacancy = vacancys
    jseeker = VacancyApply(vacancy=vacancy,user=user)
    jseeker.save()
    return redirect('JViewVacancy') 
    
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

def EduDeleteView(request,pk):
    profileobj = JseekerProfile.objects.get(education=pk)
    eduobj = JseekerEdu.objects.get(id=pk)
    profileobj.delete()
    eduobj.delete()
    return redirect('JProfile')