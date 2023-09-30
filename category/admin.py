from django.contrib import admin
from .models import Category,Subcategory

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',)}
    list_display = ('category_name', 'category_slug')
    
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'sub_category_category_slug': ('sub_category_name',)}
    list_display = ('category','sub_category_name', 'sub_category_category_slug')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)