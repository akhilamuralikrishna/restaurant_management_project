from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import MenuItem
from products.serializers import IngredientSerializer
from .serializers import MenuItemSerializer

class MenuItemIngredientsView(APIView):
    def get(self,request,menu_item_id):
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
            except MenuItem.DoesNotExist:
                return Response({'error':'menu item not found'},status=status.HTTP_404_NOT_FOUND)
            ingredients=menu_item.ingredients.all()
            serializer = IngredientSerializer(ingredients,many=True)
            return Response(serializer.data)

class UpdateMenuItem(APIView):
    def put(self, request, menu_item_id):
        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            return Response({'error':'Menu item not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                          



# Create your views here.
