from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="Jdashboard"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="JViewVacancy"),
    path("applyvacancy/<int:pk>",views.Applyvacancy,name="ApplyVacancy"),   
    path("profile/",views.jseekerprofile.as_view(),name="JProfile"),
    path("addskills/",views.jaddskills.as_view(),name="addskills"),
    path("ntomskills/<int:pk>",views.JobProfileUpdate,name="addproskills"),
    path("addedu/",views.jaddedu.as_view(),name="addedu"),
    path("ntomedu/<int:pk>",views.JobProeduUpdate,name="addproedu"),
    path("deleteskill/<int:pk>",views.SkillsDeleteView,name="skilldeleteview"),
]