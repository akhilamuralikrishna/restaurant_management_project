from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer
from django.core.paginator import import Paginator

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class FeaturedMenuItemsView(APIView):
    def get(self,request):
        items=MenuItem.objects.filter(is_featured=True)
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class SearchItemAPIView(APIView):
    def get(self,request):
        query=request.GET.get('q','')
        items=Item.objects.filter(name__icontains=query)
        paginator=Paginator(items,10)
        page_number=request.GET.get('page',1)
        page_obj=paginator.get_page(page_number)
        serializer=ItemSerializer(page_obj,many=True)
        return Response({'count':paginator.count,
        'total_pages':paginator.num_pages,
        'current_page':page_obj.number,
        'results':serializer.data},status=status.HTTP_200_OK)              
