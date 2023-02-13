from django.db import models
from phone_field import PhoneField
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# user app model.py

# Profile class 

class Profile(models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Profile creating after user registration 

@receiver(post_save, sender=User)
def send_profile_signal(sender, created, instance, **kwargs):
    """Profile creation function"""

    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
