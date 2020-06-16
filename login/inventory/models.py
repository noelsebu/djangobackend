from django.db import models

# Create your models here.


class Address(models.Model):
    line1=models.CharField(max_length=100)
    line2=models.CharField(max_length=100,blank=True, null=True)
    city=models.CharField(max_length=100,blank=True, null=True)
    state=models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.line1

class Customers(models.Model):
    address_id=models.ForeignKey(Address,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    mobilenum=models.IntegerField()
    date_joined=models.DateField(blank=True, null=True)
    date_last_purchase=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    event_type_description=models.CharField(max_length=100)


    def __str__(self):
        return self.event_type_description




    
class DocumentType(models.Model):
    document_description=models.CharField(max_length=25)

    def __str__(self):
        return self.document_description


class Staff(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField(blank=True, null=True)
    date_joined=models.DateField(blank=True, null=True)
    other_details=models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.first_name

class Supplier(models.Model):
    address_id=models.ForeignKey(Address,on_delete=models.CASCADE)
    supplier_name=models.CharField(max_length=100)
    supplier_details=models.CharField(max_length=100,blank=True, null=True)
    outstanding_amt=models.FloatField(default=0)

    def __str__(self):
        return self.supplier_name

class Product(models.Model):
    parent_product=models.ForeignKey('self',on_delete=models.CASCADE,blank=True, null=True)

    name=models.CharField(max_length=100)
    mrp=models.FloatField()
    wsp=models.FloatField()
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer_id=models.ForeignKey(Customers,on_delete=models.CASCADE,blank=True, null=True)
    transaction_type_code=models.ForeignKey(TransactionType,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    supplier_id=models.ForeignKey(Supplier,on_delete=models.CASCADE,blank=True, null=True)
    date=models.DateField()
    other_details=models.CharField(max_length=100,blank=True, null=True)
    quantity=models.IntegerField()
    
""" 
   def __str__(self):
        return self.date
"""
class Document(models.Model):
    document_type=models.ForeignKey(DocumentType,on_delete=models.CASCADE)
    transaction_id=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    date_issued=models.DateField()
    document_text=models.CharField(max_length=100,blank=True, null=True)
    other_details=models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.document_text


    

