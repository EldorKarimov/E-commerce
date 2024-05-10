from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UserMananger(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        if not email:
            raise ValidationError(_("User must be email"))
        email = self.normalize_email(email)
        user = self.model(
            email = email
        )
        user.password = make_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        user = self.create_user(
            email=email,
            password=password
        )
        user.save(using = self._db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email"), unique=True)
    address = models.TextField(_("Address"))
    phone = models.CharField(_("Phone"), max_length=13, unique=True)

    objects = UserMananger
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []