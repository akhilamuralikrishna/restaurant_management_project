from django.urls import path
from .views import FeaturedMenuItemsViews

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
]