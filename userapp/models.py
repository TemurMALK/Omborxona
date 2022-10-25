from django.contrib.auth.models import User
from django.db import models


class Sotuvchi(models.Model):
    ism = models.CharField(max_length=40)
    nom = models.CharField(max_length=40)
    manzil = models.CharField(max_length=40)
    tel = models.PositiveSmallIntegerField()
    user = models.ManyToManyField(User, null=True)
    def __str__(self):
        return f"{self.ism}, {self.nom}({self.manzil})"