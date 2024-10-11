from django.shortcuts import render

from django.http import JsonResponse
#from django.core.serializers import serialize
from rest_framework import serializers , viewsets
from .serializers import ProductSerializer
from .models import Product


#def index(request):
#    products= Product.objects.all()
#    data = serialize('python', products)
    #context = {'products': products}
    #return render(request, 'products/index.html',context)
#    return JsonResponse(data, safe=False)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer