from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('postvacancy/',views.PostVacancy.as_view(),name="Postvacancy"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="ViewVacancy"),
    path('recruiterprofile/',views.RecruiterProfileView.as_view(),name="Recruiterprofile"),
    path('recruiterprofile/updatedetails/<int:pk>/',views.RecruiterDetailsUpdateView.as_view(),name="Recruiterupdateprofile"),
]