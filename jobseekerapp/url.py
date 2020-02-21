from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="ViewVacancy"),   
]