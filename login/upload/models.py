from django.db import models

# Create your models here.
class Bill(models.Model): 
    name = models.CharField(max_length=50) 
    bill_Main_Img = models.ImageField(upload_to='images/') 