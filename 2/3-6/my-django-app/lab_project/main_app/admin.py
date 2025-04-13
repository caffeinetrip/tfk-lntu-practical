from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'description', 'is_active')
        }),
        ('Зображення', {
            'fields': ('icon',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discounted_price', 'stock_quantity', 'status', 'is_featured')
    list_filter = ('category', 'status', 'is_featured')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock_quantity', 'status', 'is_featured')
    readonly_fields = ('created_at', 'updated_at', 'discounted_price')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'category', 'description', 'price', 'discount_percentage')
        }),
        ('Склад', {
            'fields': ('stock_quantity', 'status', 'is_featured')
        }),
        ('Характеристики', {
            'fields': ('size', 'weight', 'specifications'),
            'classes': ('collapse',)
        }),
        ('Зображення', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('Службова інформація', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def discounted_price(self, obj):
        return obj.get_discounted_price()
    discounted_price.short_description = "Ціна зі знижкою"