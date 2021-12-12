from django.urls import path
from .views import signup,viewWallet,transfer

urlpatterns = [
    path("signup/",signup,name="signup"),
    path("",viewWallet,name="home"),
    path("transfer/",transfer,name="transfer"),
    path("account/<str:username>/",)
]