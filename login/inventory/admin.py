from django.contrib import admin

from .models import Address,Customers,TransactionType,Product,DocumentType,Staff,Supplier,Transaction,Document


admin.site.register(Address)
admin.site.register(Customers)
admin.site.register(TransactionType)
admin.site.register(Product)
admin.site.register(DocumentType)
admin.site.register(Staff)
admin.site.register(Supplier)
admin.site.register(Transaction)
admin.site.register(Document)

# Register your models here.

