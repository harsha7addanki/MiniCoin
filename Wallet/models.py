from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# User
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

class Gift(models.Model):
    from_usr = models.ForeignKey("User", models.CASCADE)
    ammount = models.BigIntegerField(default=10)
    message = models.TextField()

class TestModel(models.Model):
    name = models.TextField()
    msg = models.TextField()

class User(AbstractUser):
    coins = models.BigIntegerField(default=100)
    following = models.ManyToManyField("self", blank=True)
    gifts = models.ManyToManyField('Gift', blank=True)



