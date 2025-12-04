from rest_framework import serializers
from .models import Item, Ingredient, MenuItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient  
        fields = ['id','name']
class MenuItemSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many = True, read_only = True)
    Category = serializers.CharField(source = 'category.name',read_only = True)
    class Meta:
        model = MenuItem
        fields = ['id','name','category','ingredients']       


