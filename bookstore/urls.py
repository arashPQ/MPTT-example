# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryTreeView.as_view(), name='category_tree'),
]