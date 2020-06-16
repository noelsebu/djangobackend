from django.forms import ModelForm

from django.forms.models import inlineformset_factory
from .models import Product,Supplier,Transaction,Address,Customers


#
# ProductFormset = inlineformset_factory(Transaction, Product, extra=1)
TransactionFormset = inlineformset_factory(Supplier, Transaction, fields=('id',), extra=1)

class ProductModelForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class TransactionSupplierModelForm(ModelForm):
    class Meta:
        model=Transaction
        fields=['transaction_type_code','product_id','supplier_id','quantity','date','staff_id']

class SupplierModelForm(ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'

class AddressModelForm(ModelForm):
    class Meta:
        model=Address
        fields='__all__'

class CustomerModelForm(ModelForm):
    class Meta:
        model=Customers
        fields='__all__'



"""
class PurchaseForm(forms.Form):


### Supplier Model Form ###

class SupplierModelForm(ModelForm):
    class Meta:
        model=Supplier
        fields= ['']

"""



