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
