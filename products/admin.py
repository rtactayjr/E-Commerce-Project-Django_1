from django.contrib import admin

from . models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','product_name','price','stock', 'is_available','created_date', 'modified_date', 'brand',)
    prepopulated_fields = {'slug': ('product_name',)}
    
    
admin.site.register(Product, ProductAdmin)
