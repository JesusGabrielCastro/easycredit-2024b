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

    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='started')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_payments = models.IntegerField(default=1)

    def __str__(self):
        return f'Credit for {self.client} - {self.product}'