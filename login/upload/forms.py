
# forms.py 
from django import forms 
from .models import *
  
class BillForm(forms.ModelForm): 
  
    class Meta: 
        model = Bill 
        fields = ['name', 'bill_Main_Img'] 
