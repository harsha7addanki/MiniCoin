from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.set_coins(50)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password):
        user = self.create_user(
            email,
            password=password,
        )
        user.set_coins(100)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.Email(primary_key = True)
    coins = models.BigIntegerField(default=100)