from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('inv/',views.inventory,name='inventory'),
    path('checkout/',views.checkout,name='checkout'),
    path('transaction/',views.transaction,name='transaction'),
    path('report/',views.report,name='report'),
    path('chart/',views.chart,name='chart'),
]