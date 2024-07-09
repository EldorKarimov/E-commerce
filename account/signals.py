from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User, VerificationOtp
from account.utils import code_generate, send_email
from django.utils import timezone
from config.settings.base import EXPIRES_OTP_CODE

@receiver(post_save, sender=User)
def save_code(sender, instance, created, **kwargs):
    if created:
        code = code_generate()
        VerificationOtp.objects.create(
            user = instance, 
            code = code,
            type = VerificationOtp.VerificationType.REGISTER,
            expires_in = timezone.now() + timezone.timedelta(minutes=EXPIRES_OTP_CODE)
        )
        send_email(code=code, email=instance.email, user=instance)