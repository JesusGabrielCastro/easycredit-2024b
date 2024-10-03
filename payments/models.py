from django.db import models
from credits.models import Credit

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('delayed', 'Delayed'),
    ]

    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    normal_payment = models.DecimalField(max_digits=10, decimal_places=2)
    due_in = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    late_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Payment for Credit ID {self.credit.id} - Status: {self.status}'