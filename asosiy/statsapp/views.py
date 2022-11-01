from django.shortcuts import render, redirect
from django.views import *

from .models import *
from statsapp.models import *

from asosiyapp.models import *


class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            statistikalar  = Statistika.objects.all()
            word=request.POST.get('word')
            qidiruv_sozi=request.GET.get('soz')
            if qidiruv_sozi is not None:
                statistikalar = statistikalar.filter(mahsulot__nom__contains=
                qidiruv_sozi)|statistikalar.filter(mahsulot__brand__contains=
                qidiruv_sozi)|statistikalar.filter(mijoz__ism__contains=
                qidiruv_sozi)
            data={
                'stats': statistikalar
            }
            return render(request, 'stats.html', data)
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            Statistika.objects.create(
                mahsulot=Mahsulot.objects.filter(nom__contains=request.POST.get("mahsulot"))[0],
                mijoz=Mijoz.objects.filter(ism__contains=request.POST.get("mijoz"))[0],
                miqdor=request.POST.get("miqdor"),
                jami=request.POST.get("jami"),
                tolandi=request.POST.get("tolandi"),
                nasiya=request.POST.get("nasiya"),
            )
            a=Mijoz.objects.filter(ism__contains=request.POST.get("mijoz"))[0]
            a.qarz+=int(request.POST.get("nasiya"))
            a.save()
            b=Mahsulot.objects.filter(nom__contains=request.POST.get("mahsulot"))[0]
            b.miqdor-=int(request.POST.get("miqdor"))
            b.save()
            return redirect('/stats/')
        else:
            return redirect('/')