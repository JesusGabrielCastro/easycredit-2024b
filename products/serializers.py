from rest_framework import serializers
from .models import Product,ProductType

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_type= serializers.SlugRelatedField(queryset=ProductType.objects.all(),slug_field='name')
    
    class Meta:
        model = Product
        fields = ['product_type','name','price']