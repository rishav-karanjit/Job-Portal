from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="Jdashboard"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="JViewVacancy"),   
]