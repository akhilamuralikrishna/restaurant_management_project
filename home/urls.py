from django.urls import path
from .viwes import MenuCategoryListView
from home.views import MenuItemIngredientsView

urlpatterns=[
    path('menu-categories/',
    MenuCategoryListView.as_view(),
    name='menu-categories'),
    path('menu-items/<int:menu_item_id>/ingredients/',MenuItemIngredientsView.as_view()),
]