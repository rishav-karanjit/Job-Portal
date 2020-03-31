from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('',views.HomeView.as_view(),name="homepage"),
    path("Mynetwork/SuggestedUser/",views.SuggestedUser.as_view(),name="SuggestedUser"),
    path("addfriend/<int:userid>/",views.sent_friend,name="addfriend"),
    path("acceptfriend/<int:userid>/",views.accept_friend,name="acceptfriend"),
    path("Mynetwork/connectionrequest/",views.Friendrequests.as_view(),name="Friendrequests"),
    path("Mynetwork/",views.Myconnection.as_view(),name="myconnection"),
    path("Mynetworks/SuggestedProfile/ViewProfile/<int:pk>/",views.ViewSProfile.as_view(),name="ViewSProfile"),
    path("Mynetworks/ViewProfile/<int:pk>/",views.ViewProfile.as_view(),name="ViewProfile"),
    path("Mynetworks/ConnectionRequest/ViewProfile/<int:pk>/",views.ViewRProfile.as_view(),name="ViewRProfile"),
    path("search/",views.Search.as_view(),name="search"),
]