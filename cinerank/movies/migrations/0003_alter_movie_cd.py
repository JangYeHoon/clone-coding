# Generated by Django 4.2.8 on 2024-02-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cd',
            field=models.IntegerField(verbose_name='apiID'),
        ),
    ]
