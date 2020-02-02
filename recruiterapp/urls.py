from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('postvacancy/',views.PostVacancy.as_view(),name="Postvacancy"),
    path('viewvacancy/',views.ViewVacancy.as_view(),name="ViewVacancy"),
    path('recruiterprofile/',views.RecruiterProfileView.as_view(),name="Recruiterprofile"),
    path('recruiterprofile/updategeneraldetails/<int:pk>/',views.RecruiterGDetailsUpdateView.as_view(),name="Recruiterupdateprofile"),
    path('recruiterprofile/creategeneraldetails/<int:pk>/',views.RecruiterGDetailsCreateView.as_view(),name="Recruitercreateprofile"),

]