# Generated by Django 4.2.9 on 2024-02-27 11:02

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_netflixmovies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflixmovies',
            name='cast',
            field=models.JSONField(default=api.models.cast_default),
        ),
        migrations.AlterField(
            model_name='netflixmovies',
            name='description',
            field=models.TextField(default=[]),
        ),
    ]
