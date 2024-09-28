from django.contrib import admin
from .models import Credit

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'created_at', 'status')
    search_fields = ('client__first_name', 'client__last_name', 'product__name')
    list_filter = ('status', 'created_at')