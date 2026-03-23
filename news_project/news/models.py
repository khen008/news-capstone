from django.db import models
from django.contrib.auth.models import AbstractUser


class Publisher(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('reader', 'Reader'),
        ('journalist', 'Journalist'),
        ('editor', 'Editor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    subscribed_publishers = models.ManyToManyField(
        Publisher,
        blank=True,
        related_name="subscribers"
    )

    subscribed_journalists = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True
    )


class Article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="articles"
    )

    publisher = models.ForeignKey(
        Publisher,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Newsletter(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.title