from django.db import models
from userapp.models import *
from asosiyapp.models import *

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField(default=1)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    jami = models.PositiveSmallIntegerField(default=1)
    tolandi = models.PositiveSmallIntegerField(default=1)
    nasiya = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return f"{self.mahsulot},{self.mijoz},{self.sotuvchi}"