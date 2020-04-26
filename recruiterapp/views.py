from django.shortcuts import render,redirect
from django.views import generic
from .models import *
from jobseekerapp.models import *
from Jobapp.models import *
from twilio.rest import Client
from django.conf import settings

# Create your views here.
class DashboardView(generic.ListView):
    model=User
    template_name='Recruiters/dashboard.html'
    context_object_name='users'
    def get_queryset(self):
        obj=User.objects.exclude(email=self.request.user)
        return obj.filter(profession=self.request.user.profession)
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data['connection_count']=User.objects.filter(id=self.request.user.id).count()
        data['Postedvacancy']=Vacancy.objects.filter(user=self.request.user).count()
        return data
    
class PostVacancy(generic.CreateView):
    model= Vacancy
    template_name='Recruiters/postVacancy.html'
    fields=['jobcategory','title','deadline','description']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.company=self.request.user.currentcompany
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('ViewVacancy')

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

class ViewApplicants(generic.ListView):
    model=VacancyApply
    template_name='Recruiters/viewapplicants.html'
    context_object_name='applicants'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancys"] = Vacancy.objects.all()
        return context
    
    def get_queryset(self):
        return VacancyApply.objects.filter(vacancy__user=self.request.user.id,status=1)

def ViewAProfile(request, pk):
    context={}
    context['data']=JseekerProfile.objects.filter(user_id=pk)
    return render(request,"profileAView.html",context)

def AcceptApplicants(request, pk):
    applicants = VacancyApply.objects.get(id=pk)
    applicants.status = 2
    applicants.save()
    to='+91'+applicants.user.Mobile_Number
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    response = client.messages.create(
                body='Your Application for vacancy: '+applicants.vacancy.title+' is Accepted', 
                to=to, from_=settings.TWILIO_PHONE_NUMBER)
    return redirect('Viewappli')

def RejectApplicants(request, pk):
    applicants = VacancyApply.objects.get(id=pk)
    applicants.status = 3
    applicants.save()
    return redirect('Viewappli')