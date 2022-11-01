from django.shortcuts import render, redirect
from django.views import *

from .models import *
from userapp.models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect('/')

class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'mahsulot':Mahsulot.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'products.html', data)
        else:
            return redirect('/')
    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get("nom"),
                brand=request.POST.get("brand"),
                narx=request.POST.get("narx"),
                miqdor=request.POST.get("miqdor"),
                sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
            )
            return redirect('/bolimlar/mahsulotlar/')
        else:
            return redirect('/')

class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'clients':Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'clients.html', data)
        else:
            return redirect('/')
    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                nom=request.POST.get("nom"),
                ism=request.POST.get("ism"),
                manzil=request.POST.get("manzil"),
                tel=request.POST.get("tel"),
                qarz=request.POST.get("qarz"),
                sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
            )
            return redirect('/bolimlar/clientlar/')
        else:
            return redirect('/')

class ProductDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi=Sotuvchi.objects.get(user=request.user)
            m = Mahsulot.objects.get(id=pk)
            if m.sotuvchi == hozirgi_sotuvchi and request.user.is_staff:
                m.delete()
            return redirect('mahsulotlar')
        return redirect('/')

class ClientDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi=Sotuvchi.objects.get(user=request.user)
            m = Mijoz.objects.get(id=pk)
            if m.sotuvchi == hozirgi_sotuvchi and request.user.is_staff:
                m.delete()
                return redirect('/bolimlar/clientlar/')
        else:
            return redirect('/')

class ClientupdateView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi=Sotuvchi.objects.get(user=request.user)
            m=Mijoz.objects.get(id=pk)
            if m.sotuvchi == hozirgi_sotuvchi and request.user.is_authenticated:
                data={
                    "mijoz":m
                }
                return render(request, 'client_update.html', data)
            else:
                return redirect('/bolimlar/clientlar/')

    def post(self, request, pk):
        Mijoz.objects.filter(id=pk).update(
            nom=request.POST.get("nom"),
            ism=request.POST.get("ism"),
            manzil=request.POST.get("manzil"),
            tel=request.POST.get("tel"),
            qarz=request.POST.get("qarz")
        )
        return redirect('/bolimlar/clientlar/')

class ProductupdateView(View):
    def get(self, request, pk):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and hozirgi_ombor == product.sotuvchi:
            data = {
                'mahsulot':product
            }
            return render(request, 'product_update.html', data)
        else:
            return redirect('/bolimlar/mahsulotlar/')

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
                nom=request.POST.get("nom"),
                brand=request.POST.get("brand"),
                narx=request.POST.get("narx"),
                miqdor=request.POST.get("miqdor")
        )
        return redirect('/bolimlar/mahsulotlar')
