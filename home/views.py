from django.shortcuts import render
from rest_framework.views import API
from rest_framework.response import Response
from products.models import MenuItem
from products.serializers import IngredientSerializer
class MenuItemIngredientsView(APIView):
    def get(self,request,menu_item_id):
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
            except MenuItem.DoesNotExist:
                return Response({'error':'menu item not found'},status=status.HTTP_404_NOT_FOUND)
            ingredients=menu_item.ingredients.all()
            serializer = IngredientSerializer(ingredients,many=True)
            return Response(serializer.data)   



# Create your views here.
