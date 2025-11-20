from django.urls import path
from .views import ItemView ,FeaturedMenuItemsView
from .views import SearchItemAPIView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('featured_items/',FeaturedMenuItemsView.as_view(),name='featured_items'),
    path('search-items/',SearchItemAPIView.as_viwe())
]