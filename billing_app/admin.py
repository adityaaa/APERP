# billing_app/admin.py
from django.contrib import admin
from .models import Manufacturer, InventoryItem, Salt

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Define search_fields for ManufacturerAdmin

@admin.register(Salt)
class SaltAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Define search_fields for SaltAdmin    

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'packing', 'mrp', 'salt', 'category', 'rate', 'conversion_strip', 'conversion_case', 'sgst', 'cgst')
    list_filter = ('company', 'salt', 'category')
    search_fields = ('name', 'company__name', 'salt__name', 'category')
    autocomplete_fields = ('company', 'salt')
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'packing', 'salt', 'category', 'mrp', 'rate', 'conversion_strip', 'conversion_case', 'sgst', 'cgst'),
        }),
    )