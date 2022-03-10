from django.db.models.signals import post_save
from django.dispatch import receiver
from teachers.models import Teacher
import django.dispatch

teacher_created = django.dispatch.Signal()


@receiver(post_save, sender=Teacher)
def save_profile(sender, instance, created, **kwargs):
    if created:
        print(f'Teacher {instance} created')
