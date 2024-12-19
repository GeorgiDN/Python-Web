from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from forumApp.posts.models import Post


@receiver(post_save, sender=Post)
def send_approval_notification(sender, instance, created, **kwargs):
    if not created and instance.approved:
        send_mail(
            subject="Your post is approved",
            message=f"Hi {instance.author.username}, \n\nYour post has been approved.",
            from_email="forumAppEmail@forum.com",  # just example
            recipient_list=[instance.author.email],
        )
