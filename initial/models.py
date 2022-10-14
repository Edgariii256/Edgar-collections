from django.db import models

# Create your models here.


class Commodities(models.Model):
    
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)

class Shop(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField()
    brk=models.BooleanField(default=False)