from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from .managers import UserManager
from common.models import BaseModel
from django.core.validators import RegexValidator

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    email = models.EmailField(_("Email"), unique=True)
    phone = models.CharField(_("Phone"), max_length=13, validators=[
        RegexValidator(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'),
    ],
    help_text=_(
            "Enter a valid phone number"
        ),
        )
    address = models.TextField(_("Address"))

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class VerificationOtp(BaseModel):
    class VerificationType(models.TextChoices):
        REGISTER = 'register', _("Registraion")
        RESET_PASSWORD = 'reset_password', _("Reset password")
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    code = models.IntegerField(_("Code"))
    type = models.CharField(_("Verification Type"), choices=VerificationType.choices)
    expires_in = models.DateTimeField(_("Expiration time"))

    def __str__(self):
        return f"{self.user.email} - {self.code}"

    class Meta:
        verbose_name = _("Verification Otp")
        verbose_name_plural = _("Verification Otps")


class UserAddress(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name="Name")
    phone_number = models.CharField(max_length=13, verbose_name="Phone number", validators=[
        RegexValidator(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    ])
    apartment = models.CharField(max_length=120, verbose_name="Apartment")
    street = models.TextField(_("Street"))
    pin_code = models.CharField(_("Pin code"), max_length = 20)
    city = models.ForeignKey('common.Region', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.name}"

    class Meta:
        verbose_name = _("User address")
        verbose_name_plural = _("User addresses")