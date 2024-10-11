from django.urls import path
#from . import  views
from .views import ProductViewSet
urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name="index"),
    
]
