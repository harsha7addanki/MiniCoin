from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import *

class SignUpForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User 
        fields = ('username','email','password1', 'password2',)