from django.db import models

# Create your models here.
class Movie(models.Model):
    cd = models.IntegerField("apiID")
    name = models.TextField("영화제목")
    thumbnail = models.TextField("thumbnail", blank=True)
    def __str__(self):
        return self.name

class Rank(models.Model):
    cd = models.IntegerField("apiID")
    date_week = models.BooleanField("일간 or 주간")
    rank = models.IntegerField("순위")
    name = models.TextField("영화제목")
    date = models.DateField("요청날짜")
    audi_cnt = models.IntegerField("관객수")
    audi_acc = models.IntegerField("누적관객수")
    thumbnail = models.TextField("thumbnail")