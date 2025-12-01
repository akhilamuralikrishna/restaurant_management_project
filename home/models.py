from django.db import models
from datetime import date

class MenuCategory(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class DailySpecialManager(models.Manager):
    def upcoming(self):
        today = date.today()
super().get_queryset().filter(special_date__get=today) 


class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    special_date=models.DateField()
    objects=DailySpecialManager()
    def __str__(self):
        return self.name
    @staticmethod 
    def get_random_special():
        specials=DailySpecial.objects.all()
        
        if not specials.exists():
            return None
        return specials.order_by('?').first()      #Create your models here.

