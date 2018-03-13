from django.db.models.signals import post_save
from app.account.models import User, UserDetails
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_details(instance, created, **kwargs):
    if created:
        user_details = UserDetails()
        user_details.user = instance
        user_details.first_name = instance.first_name
        user_details.last_name = instance.last_name
        user_details.save()



