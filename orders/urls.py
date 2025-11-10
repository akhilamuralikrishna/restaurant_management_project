from django.urls import path
from .views import CoupleValidationView

urlpatterns = [ path('validate/',CoupleValidationView.as_view(),name='coupon-validate')

    
]