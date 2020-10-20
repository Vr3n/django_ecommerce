from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from shop.models import Customer

from .models import CustomUser

# Create Customer on creation of User.


def create_customer_profile(sender, instance, created, **kwargs):

    if created:
        group = Group.objects.get(name="customer")
        instance.groups.add(group)
        
        Customer.objects.create(
            user=instance,
            name=instance.first_name,
        )

        print('User and Customer Created!')


# Connecting post_save to create_customer_profile when User model is triggered.

post_save.connect(create_customer_profile, sender=CustomUser)


# Updating customer on updation of user.

def update_customer_profile(sender, instance, created, **kwargs):

    if not instance.is_superuser:
        if created == False:
            instance.customer.name = instance.first_name
            instance.customer.save()
            print('User and Customer Updated')

post_save.connect(update_customer_profile, sender=CustomUser)