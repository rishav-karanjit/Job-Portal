from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('verification/',views.VerificationView.as_view(),name="VerificationView"),
]