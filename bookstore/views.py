# views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

class CategoryTreeView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context