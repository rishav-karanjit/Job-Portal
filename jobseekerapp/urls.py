from django.urls import path
from . import views

urlpatterns = [
    path('jdashboard/',views.DashboardView.as_view(),name="Jdashboard"),
    path('jviewvacancy/',views.ViewVacancy.as_view(),name="JViewVacancy"),   
]