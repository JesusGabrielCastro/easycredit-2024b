from django.contrib import admin
from .models import Client, Employee, Admin

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'job_title', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role')
    search_fields = ('first_name', 'last_name', 'email')