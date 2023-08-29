from django.contrib import admin

from catalog.models import Category, Product, Version, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'price', 'category', 'owner']
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """Админ-панель для работы с моделью Version"""

    list_display = ['product', 'number', 'title', 'is_active']
