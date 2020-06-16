from django.shortcuts import render
from django.db import models
from django.forms import modelformset_factory

from django.http import HttpResponse
from .models import Product,Supplier
from .forms import ProductModelForm,TransactionSupplierModelForm,SupplierModelForm,CustomerModelForm,AddressModelForm




# Create your views here.
def product_view(request):
    products_list=Product.objects.all()
    context = {'products_list': products_list}
    return render(request,'product_view.html',context)

def  product_add(request):

    
    form_class=ProductModelForm(request.POST)

    if form_class.is_valid():

            product = form_class.save()
    return render(request,'add_product.html',{'form': form_class})


def  supplier_add(request):

    
    form_class=SupplierModelForm(request.POST)

    if form_class.is_valid():

            supplier = form_class.save()
    return render(request,'add_supplier.html',{'form': form_class})

def address_add(request):

    form_class=AddressModelForm(request.POST)

    if form_class.is_valid():

            address = form_class.save()
    return render(request,'add_address.html',{'form': form_class})

def customer_add(request):

    form_class=CustomerModelForm(request.POST)

    if form_class.is_valid():

            customer = form_class.save()
    return render(request,'add_customer.html',{'form': form_class})

def transaction_supplier_add(request):

    form_class=TransactionSupplierModelForm(request.POST)

    if form_class.is_valid():

            transaction = form_class.save()
    return render(request,'add_transaction_supplier.html',{'form': form_class})


