from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, password=None):
        user = self.model(
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
    coins = models.BigIntegerField(default=100)
    following = models.ManyToManyField("self")