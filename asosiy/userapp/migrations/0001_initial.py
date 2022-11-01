# Generated by Django 4.1.2 on 2022-10-28 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=90)),
                ('tel', models.CharField(max_length=20)),
                ('user', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
