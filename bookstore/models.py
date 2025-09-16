from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

'''

    This project just shows you how MPTT works. How you use it in your projects is up to you. I tried to give a very simple example. You can implement more advanced topics by reading the documentation.
    "https://django-mptt.readthedocs.io/"
    Front-end optimization is up to you :)

'''

class Category(MPTTModel):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name