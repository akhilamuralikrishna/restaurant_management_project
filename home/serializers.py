from rest_frmework import serializers
from .models import MenuCategory
from .models import MenuItem

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields=['id','name']
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name','description','price','available']

    def validate_price(self,value):
        if value <= 0:
            raise serializer.ValidationError('Price must be positive.')
        return value               