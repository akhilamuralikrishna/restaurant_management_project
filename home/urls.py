from django.urls import path
from .viwes import MenuCategoryListView
from home.views import MenuItemIngredientsView
from .views import UpdateMenuItem

urlpatterns=[
    path('menu-categories/',
    MenuCategoryListView.as_view(),
    name='menu-categories'),
    path('menu-items/<int:menu_item_id>/ingredients/',MenuItemIngredientsView.as_view()),
    path('menu/update/<int:menu_item_id>/')
]