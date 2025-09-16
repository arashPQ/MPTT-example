from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models

@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'slug', 'parent', 'level']
    list_filter = ['parent']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    mptt_level_ident = 20
    
    mptt_ident_fields = "name"