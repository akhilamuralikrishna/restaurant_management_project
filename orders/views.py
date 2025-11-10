from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIview
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon

class CouponValidationView(APIview):
    def post(self,request)
    code=request.data.get('code')

    if not code:
        return Response({'error':'coupon code is rquired'},status=status.HTTP_400_BAD_REQUEST)
    try:
        coupon=Coupon.Objects.get(code=code)
    except Coupon.DoesNotExist:
        return Response({'Error':'Invalid Coupon Code'},status=status.HTTP_404_NOT_REQUEST)
        if coupon.is_valid():
            return Response({
                'success':True,
                'message':'couple is valid',
                'discount':float(coupon.discount)
            },status=status.HTTP_200_OK)
        return Response({'error':'Coupon expired or inactive'},status=status.HTTP_400_BAD_REQUEST)            