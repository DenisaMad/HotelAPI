from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from TMHotelConnectAPI.utils import Send_email_handler


@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user=instance.user
    user.delete()




