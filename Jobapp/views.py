from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.views.generic.base import TemplateView
from recruiterapp.models import *
from .form import *
from django.db.models import Q

# Create your views here.

class SignUpView(generic.CreateView):
    form_class=Signupform
    template_name='registration/signup.html'
    success_url=reverse_lazy('homepage')

class HomeView(generic.ListView):
    model=Vacancy
    template_name='home.html'
    context_object_name='vacancys'
    def get_queryset(self):
        return Vacancy.objects.all()

class Search(generic.ListView):
    def get(self, request, *args, **kwargs):
        search_term=request.GET['search_term']
        Category=request.GET['Category']
        Company=request.GET['Company']
        if(search_term==''):
            search_term="Novalue"
        
        search_result=Vacancy.objects.filter(Q(title__icontains=search_term) | Q(jobcategory=Category) | Q(company=Company))
        context={
            'search_term': search_term,
            'Category':Category,
            'Company':Company,
            'vacancys':search_result
        }
        return render(request,'search.html',context)

class SuggestedUser(generic.ListView):
    model=User
    template_name='Suggestedconnection.html'
    context_object_name='users'
    def get_queryset(self):
        obj=User.objects.exclude(email=self.request.user)
        return obj.filter(profession=self.request.user.profession)

def sent_friend(request, userid):
    user = User.objects.get(id=userid)
    frequest.objects.get_or_create(from_person=request.user,to_person=user)
    return redirect('myconnection')

def accept_friend(request, userid):
    from_user = get_object_or_404(User,id=userid)
    to_user= get_object_or_404(User,id=request.user.id)
    print(from_user)
    print(to_user)
    friendrequest = frequest.objects.filter(from_person=from_user,to_person=request.user).first()
    from_user.connections.add(to_user)
    to_user.connections.add(from_user)
    friendrequest.delete()
    return redirect('myconnection')

class Friendrequests(generic.ListView):
    model=frequest
    template_name="friendrequests.html"
    context_object_name='requests'

    def get_queryset(self):
        return frequest.objects.filter(to_person=self.request.user.id)

class Myconnection(generic.ListView):
    model=User
    template_name="myconnections.html"
    context_object_name='myself'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class ViewProfile(generic.DetailView):
    model=User
    template_name="ProfileView.html"
    context_object_name='profile'

class ViewRProfile(generic.DetailView):
    model=User
    template_name="ProfileRView.html"
    context_object_name='profile'

class ViewSProfile(generic.DetailView):
    model=User
    template_name="ProfileSView.html"
    context_object_name='profile'
