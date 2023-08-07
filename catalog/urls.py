from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import home, contacts, products

app_name = "catalog"

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', products, name='products')
]