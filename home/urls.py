from django.urls import path
from .viwes import MenuCategoryListView

urlpatterns=[
    path('menu-categories/',
    MenuCategoryListView.as_view(),
    name='menu-categories'),
]