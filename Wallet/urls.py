from django.contrib import admin
from django.urls import path,include
from .views import signup,viewWallet,transfer,userpage,collectgift

urlpatterns = [
    path("signup/",signup,name="signup"),
    path("",viewWallet,name="home"),
    path("transfer/",transfer,name="transfer"),
    path("account/<str:username>/",userpage),
    path("collectgift/<int:id>/",collectgift,name="colgift"),
    path('admin/', include("admin.site.urls")),
]