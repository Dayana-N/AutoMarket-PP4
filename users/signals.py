from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    Signal to create profile when
    new user is created
    '''
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            name=user.first_name,
            email=user.email,
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    '''
    Signal to delete user when
    profile is deleted from admin
    '''
    user = instance.user
    user.delete()


@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    '''
    Signal to update user profile
    '''
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
