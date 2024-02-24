from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    like_movies = models.ManyToManyField(
        "movies.Movie",
        verbose_name="좋아요 누른 Movie 목록",
        related_name="like_users",
        blank=True,
    )
    def __str__(self):
        return self.username