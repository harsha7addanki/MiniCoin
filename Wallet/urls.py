from django.urls import path
from .views import signup,viewWallet

urlpatterns = [
    path("signup/",signup),
    path("",viewWallet,name="home")
]