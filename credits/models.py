from django.db import models
from users.models import Client
from products.models import Product

class Credit(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='started')

    def __str__(self):
        return f'Credit for {self.client} - {self.product}'