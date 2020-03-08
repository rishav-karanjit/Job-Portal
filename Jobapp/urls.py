from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('',views.HomeView.as_view(),name="home"),
    path("SuggestedUser/",views.SuggestedUser.as_view(),name="SuggestedUser"),
    path("addfriend/<int:userid>/",views.sent_friend,name="addfriend"),
    path("acceptfriend/<int:userid>/",views.accept_friend,name="acceptfriend"),
    path("friendrequest/",views.Friendrequests.as_view(),name="Friendrequests"),
    path("myconnection/",views.Myconnection.as_view(),name="myconnection"),
]