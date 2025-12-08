from django.db import models
from django.db.models import Count

# Create your models here.
class MenuItemManager(models.Manager):
    def top_selling(self, num_items=5):
        return self.annotate(total_orders=Count('orderitem')).order_by('-total-orders')[:num_items]

class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return str(self.item_name)
class NeutritionalInformation(models.Model):
    menu_item=models.ForeignKey(MenuIten,on_delete=models.CASCADE)
    calories=models.IntegerField()
    protein_grams=models.DecimalField(max_digits=5,decimal_places=2)
    fat_grams=models.DecimalField(max_digits=5,decimal_places=2)
    carbohydrates_grams=DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return f'{self.menu_item.item_name}-{self.calories}calories'
class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name        
class MenuItem(models.Model):
    name = models.CharField(max_length = 100)
    ingredients = models.ManyToManyField(Ingredient,related_name='menu_items')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='menu_item')
    objects = MenuItemManager()

    def __str__(self):
        return self.name

        