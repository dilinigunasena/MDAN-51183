from django.db import models

# Create your models here.

class inventory(models.Model):
    model_number = models.CharField(max_length=25,primary_key=True)
    model_name = models.CharField(max_length=25)
    make =  models.CharField(max_length=10)
    yom = models.DateField(blank=True,null=True)     
    unit_price = models.FloatField()
    quantity_avl = models.IntegerField()
    quantity_sold = models.IntegerField(blank=True,null=True)