# Generated by Django 4.1.2 on 2022-10-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='kelgan_sana',
            field=models.DateField(auto_now_add=True),
        ),
    ]
