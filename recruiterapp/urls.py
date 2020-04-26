from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="RDashboard"),
    path('postvacancy/',views.PostVacancy.as_view(),name="Postvacancy"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="ViewVacancy"),
    path('recruiterprofile/',views.RecruiterProfileView.as_view(),name="Recruiterprofile"),
    path('recruiterprofile/updatedetails/<int:pk>/',views.RecruiterDetailsUpdateView.as_view(),name="Recruiterupdateprofile"),
    path('applicants/',views.ViewApplicants.as_view(),name="Viewappli"),
    path("ViewAProfile/<int:pk>/",views.ViewAProfile,name="ViewAProfile"),
    path("Accept/<int:pk>/",views.AcceptApplicants,name="AcceptAppli"),
    path("Reject/<int:pk>/",views.RejectApplicants,name="RejectAppli"),
]