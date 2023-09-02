from django.conf import settings
from django.core.cache import cache

from catalog.models import Category, Product


def get_cashed_products_list(object_id):
    if settings.CACHE_ENABLED:
        key = f'product_{object_id}'
        product_list = cache.get(key)

        if product_list is None:
            product_list = Product.objects.filter(id=object_id)
            cache.set(key, product_list)

    else:
        product_list = Product.objects.filtet(id=object_id)

    return product_list


def get_cashed_categories_list():
    if settings.CACHE_ENABLED:
        key = 'categories'
        categories_list = cache.get(key)

        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)

    else:
        categories_list = Category.objects.all()

    return categories_list
