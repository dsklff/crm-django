from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


# this methods need to be in signals.py file
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


# post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created is False:
        instance.profile.save()
        print('Profile updated!')


# post_save.connect(update_profile, sender=User)





# apps.py file configuration(remember to add to INSTALLED_APPS(settings.py) path to our config(accounts.apps.AccountsConfig)
# from django.apps import AppConfig
#
# class AccountsConfig(AppConfig):
#     name = 'accounts'
#
#     def ready(self):
#         import accounts.signals


#or you can add to __init__.py the (default_app_config = 'accounts.apps.AccountsConfig')
