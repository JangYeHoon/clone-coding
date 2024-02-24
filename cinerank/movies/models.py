from django.db import models

# Create your models here.
class Movie(models.Model):
    cd = models.IntegerField("apiID")
    name = models.TextField("영화제목")
    def __str__(self):
        return self.name