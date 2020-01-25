from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('',views.HomeView.as_view(),name="home"),
]