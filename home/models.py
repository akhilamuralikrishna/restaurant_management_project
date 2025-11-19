from django.db import models

class MenuCategory(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return self.name
    @staticmethod 
    def get_random_special():
        specials=DailySpecial.objects.all()
        
        if not specials.exists():
            return None
        return specials.order_by('?').first()      #Create your models here.

