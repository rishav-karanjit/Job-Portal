from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('postvacancy/',views.PostVacancy.as_view(),name="Postvacancy"),
    path('recruiterprofile/',views.RecruiterProfileView.as_view(),name="Recruiterprofile"),
    path('recruiterprofile/updategeneraldetails/<int:pk>/',views.RecruiterGDetailsUpdateView.as_view(),name="Recruiterupdateprofile"),
    path('recruiterprofile/creategeneraldetails/<int:pk>/',views.RecruiterGDetailsCreateView.as_view(),name="Recruitercreateprofile"),
]