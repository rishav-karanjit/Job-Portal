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
class RecruiterProfileView(generic.ListView):
    model=User
    template_name='RecruiterProfile.html'
    context_object_name = 'Recruiters' 

    def get_context_data(self, **kwargs):
        context = super(RecruiterProfileView, self).get_context_data(**kwargs)
        context['additional_profile'] = recruiterprofile.objects.all()#filter(user_id=self.request.user)