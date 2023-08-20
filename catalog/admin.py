from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'price', 'category']
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """Админ-панель для работы с моделью Version"""

    list_display = ['product', 'number', 'title', 'is_active']
