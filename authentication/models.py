from enum import unique
from operator import rshift
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError(_("Email Should be Provided"))
        email = self.normalize_email(email)
        new_user = self.model(email= email,**extra_field)
        new_user.set_password(password)
        new_user.save()
        return new_user

    
    def create_superuser(self, email, password, **extrafields):
        user = self.create_superuser(email=email, password=password, **extrafields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"<User {self.email}"