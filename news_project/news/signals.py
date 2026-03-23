from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import requests

from .models import Article, CustomUser


@receiver(post_save, sender=Article)
def article_approved(sender, instance, created, **kwargs):

    if instance.approved:

        subscribers = []

        if instance.publisher:

            subscribers += list(
                instance.publisher.subscribers.all()
            )

        subscribers += list(
            CustomUser.objects.filter(
                subscribed_journalists=instance.author
            )
        )

        emails = [u.email for u in subscribers]

        send_mail(
            "New Article Published",
            instance.title,
            "admin@news.com",
            emails,
            fail_silently=True
        )

        requests.post(
            "http://127.0.0.1:8000/api/approved/",
            json={"article": instance.title}
        )