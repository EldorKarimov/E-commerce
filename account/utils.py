import random
from django.core.mail import send_mail

from config.settings import base

def code_generate():
    nums = [1,2,3,4,5,6,7,8,9,0]
    return ''.join([str(random.choice(nums)) for i in range(6)])

def send_email(code, email, user):
    send_mail(
        subject=f"Hello {user.get_full_name}",
        message=f"your activation code is {code}",
        from_email=base.EMAIL_HOST_USER,
        recipient_list=[email]
    )