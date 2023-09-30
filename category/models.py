from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField(max_length=100, unique=True)
    category_description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categorys'
        verbose_name_plural = 'Categories'
        
    
    # def get_absolute_url(self):
    #     return reverse('product_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    sub_category_name = models.CharField(max_length=100)
    sub_category_category_slug = models.SlugField(max_length=100, unique=True)
    sub_category_description = models.TextField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subcategorys'
        verbose_name_plural = 'Sub-Categories'
        
    def __str__(self):
        return self.sub_category_name