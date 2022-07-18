from django.db import models


class Transformer(models.Model):
    Repository =  models.TextField(max_length=1000)
    Stars =  models.IntegerField(null=True)
    Contributors = models.IntegerField(null=True)
    Programming_Language =  models.TextField(max_length=1000, help_text="Programming Language")




class ElectricityBill(models.Model):
    consumer_no	= models.CharField(max_length=500)
    Billing_Month = models.CharField(max_length=6)
    current_bill_amount= models.FloatField()
    previous_bill_amount= models.FloatField()	
    units_consumed=models.IntegerField(null=True)
    consumer_name = models.CharField(max_length=500)