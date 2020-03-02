from django.urls import path
from . import views

urlpatterns = [
    path('jdashboard/',views.DashboardView.as_view(),name="Jdashboard"),
    path('jviewvacancy/',views.ViewVacancy.as_view(),name="JViewVacancy"),
    path("japplyvacancy/<int:pk>",views.Applyvacancy,name="ApplyVacancy"),   
    path("jprofile/",views.jseekerprofile.as_view(),name="JProfile"),
    path("jaddskills/",views.jaddskills.as_view(),name="addskills"),
    path("jntomskills/<int:pk>",views.JobProfileUpdate,name="addproskills"),
]