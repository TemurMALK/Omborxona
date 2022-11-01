from django.db import models
from userapp.models import *


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    miqdor = models.PositiveSmallIntegerField()
    brand = models.CharField(max_length=50)
    kelgan_sana = models.DateField(auto_now_add=True)
    olchov = models.CharField(max_length=30, default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom}, {self.brand}"

class Mijoz(models.Model):
    nom = models.CharField(max_length=50)
    ism = models.CharField(max_length=50)
    manzil = models.CharField(max_length=90)
    tel = models.CharField(max_length=20)
    qarz = models.PositiveSmallIntegerField(default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom}, {self.ism}"