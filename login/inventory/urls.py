from django.urls import path
from . import views

urlpatterns = [
    path('inventory',views.product_view,name='inventory'),
    path('add_product',views.product_add,name='add_product'),
    path('add_supplier',views.supplier_add,name='add_supplier'),
    path('add_customer',views.customer_add,name='add_customer'),
    path('add_address',views.address_add,name='add_address'),
    path('add_transaction_supplier',views.transaction_supplier_add,name='add_transaction_supplier')
]