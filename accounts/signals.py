from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import *


def customer_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('Profile was created!')


post_save.connect(customer_profile, sender=User)
