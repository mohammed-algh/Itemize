from django.contrib import admin

# Register your models here.
from .models import Category, Item
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
    plural_name = "Categories"

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'purchase_date', 'price', 'location', 'created_at', 'updated_at')
    list_filter = ('category', 'purchase_date', 'warranty_expiry', 'location')
    search_fields = ('name', 'description', 'serial_number', 'location')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'quantity', 'image')
        }),
        ('Purchase Information', {
            'fields': ('purchase_date', 'price', 'serial_number', 'warranty_expiry')
        }),
        ('Location & Notes', {
            'fields': ('location', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )