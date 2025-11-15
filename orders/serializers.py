from rest_framework impot serializers
from .models import Order
from products.models import products

class ProductSerializer(serializer.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']
class OrderSerializer(serializers.ModelSerializer):
    items=ProductSerializer(many=True)

    class Meta:
        model=Order
        fields=['id','order_rate','otal_price','items']
