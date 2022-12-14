# Generated by Django 4.1.2 on 2022-10-10 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=40)),
                ('manzil', models.CharField(max_length=40)),
                ('tel', models.CharField(max_length=30)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('narx', models.PositiveSmallIntegerField()),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('brend', models.CharField(max_length=40)),
                ('kelgan_sana', models.DateField()),
                ('olchov', models.CharField(max_length=40)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
    ]
