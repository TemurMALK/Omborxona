from django.shortcuts import render, redirect
from django.views import View
from .models import *


class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            statistikalar = Static.objects.filter(sotuvchi__user=request.user)
            qidiruv_sozi = request.GET.get('soz')
            if qidiruv_sozi is not None:
                statistikalar = statistikalar.filter(mahsulot__nom__contains=qidiruv_sozi)

            data = {
                'statistika':statistikalar
            }
            return render(request, 'stats.html', data)
        else:
            return redirect('/')
