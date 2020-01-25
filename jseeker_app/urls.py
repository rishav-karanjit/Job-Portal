from django.urls import path
from . import views
urlpatterns = [
    path('postvacancy/',views.PostVacancy.as_view(),name="PostVacancy"),
    #path('verification/',views.VerificationView.as_view(),name="VerificationView"),
]