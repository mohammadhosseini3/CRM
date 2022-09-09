from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer
from django.dispatch import receiver
#for registering customer
from django.contrib.auth.models import Group

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    # print(instance,sender,created)
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        #create a group on registeration
        # create a customer from user
        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('Profile created!')
@receiver(post_save,sender=Customer)
def update_profile(sender,instance,created,**kwargs):
    #user already exists
    if created == False:
        instance.user.save()
        print('Profile updated!')