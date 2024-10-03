from django.contrib import admin
from .models import ProductType, Product

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)      

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'product_type')  
    search_fields = ('name',)                               
    list_filter = ('product_type',)                         