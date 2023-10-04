from django.db import models
from django.urls import reverse
from django.db.models import Avg, Count


from accounts.models import Account
from category.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.PositiveIntegerField()
    is_available    = models.BooleanField(default=True)
    brand           = models.CharField(max_length=100, blank=True)
    
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    # discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # sizes = models.CharField(max_length=100, blank=True, help_text="Enter available sizes separated by commas")
    # colors = models.CharField(max_length=100, blank=True, help_text="Enter available colors separated by commas")
    # related_products = models.ManyToManyField('self', blank=True, related_name='related_products')
    # tags = models.ManyToManyField('Tag', blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.category_slug, self.slug])

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects  =  VariationManager()

    def __str__(self):
        return self.variation_value
    