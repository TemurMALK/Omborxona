# Generated by Django 4.1.2 on 2022-10-12 07:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0002_remove_sotuvchi_vazifa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotuvchi',
            name='user',
        ),
        migrations.AddField(
            model_name='sotuvchi',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
