from django.urls import path
from .views import signup,viewWallet,transfer,userpage,collectgift,givegift

urlpatterns = [
    path("signup/",signup,name="signup"),
    path("",viewWallet,name="home"),
    path("transfer/",transfer,name="transfer"),
    path("account/<str:username>/",userpage),
    path("collectgift/<int:id>/",collectgift,name="colgift"),
    path("givegift/",givegift,name="givegift"),
]