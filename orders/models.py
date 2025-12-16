from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.
class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
@receiver(post_migrate)
def add_default_statuses(sender,**kwargs):
    if sender.name=='orders':
        statuses=['PENDING','PROCESSING','COMPLETED','CANCELLED']
        for status in statuses:
            OrderStatus.objects.get__or__create(name=status)

from django.utils import timezone

class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount=models.DecimalField(max_digits=5,decimal_place=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateTimeField()
    valid_to=models.DataTimeField()

    def __str__(self):
        return self.code
    def is_valid(self):
        now=timezone.now()
        return self.is_active and self.valid_from<=now<=self.valid_to 

class OrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])
class Order(models.Model):
    STATUS_CHOICES =[
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]
    order_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES)

    objects=OrderManager()
    def __str__(self):
        return self.order_name       

