from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must be email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields['is_staff'] is not True:
            raise ValueError("is_staff must be True")
        if extra_fields['is_superuser'] is not True:
            raise ValueError("is_superuser must be True")
        return self.create_user(email=email, password=password, **extra_fields)