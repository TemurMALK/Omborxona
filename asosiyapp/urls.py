from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('pr_delete/<int:pk>/', MahsulotDeleteView.as_view(), name='product_delete'),
    path('pr_update/<int:pk>/', MahsulotUpdateView.as_view(), name='product_update'),
    path('clientlar/update/<int:pk>', ClientupdateView.as_view(), name='client_update'),
    path('cl_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('clientlar/', ClientView.as_view(), name='clientlar'),
]