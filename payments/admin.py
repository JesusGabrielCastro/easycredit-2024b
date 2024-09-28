from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'credit', 'normal_payment', 'due_in', 'status', 'late_payment')
    search_fields = ('credit__id',)
    list_filter = ('status', 'due_in')