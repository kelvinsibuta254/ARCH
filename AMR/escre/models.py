from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Override an email field
# override username field
#create a user manager
#register the Staff model with django admin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Staff(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=20)

    USERNAME_FIELD = "username"

    #REQUIRED_FIELDS = []