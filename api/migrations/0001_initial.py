# Generated by Django 4.2.9 on 2024-01-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactEnroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, default='No message', null=True)),
            ],
        ),
    ]
