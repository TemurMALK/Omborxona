# Generated by Django 4.1.2 on 2022-10-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotuvchi',
            name='vazifa',
        ),
    ]
